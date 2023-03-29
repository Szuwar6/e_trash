from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View

from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    FormView,
    CreateView,
)

from base.forms import ClientForm, AddressForm, RecyclerForm, OrderForm
from base.models import Client, Address, Recycler, Order


class ClientAddressCreateView(LoginRequiredMixin, CreateView):
    template_name = "client_address.html"
    form_class = ClientForm
    success_url = reverse_lazy("base:clients-detail-view")

    def form_valid(self, form):
        context = self.get_context_data()
        form_2 = context["form_2"]
        if form_2.is_valid():
            client = form.save(commit=False)
            client.user = self.request.user
            client.save()
            address = form_2.save(commit=False)
            address.user = self.request.user
            address.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, form_2=form_2)
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["form_2"] = AddressForm(self.request.POST)
        else:
            context["form_2"] = AddressForm()
        return context


class CurrentUserMixin(object):
    model = Client

    def get_object(self, *args, **kwargs):
        return self.request.user.client


class CurrentAddressMixin(object):
    model = Address

    def get_object(self, *args, **kwargs):
        return self.request.user.address


class CurrentRecyclerMixin(object):
    model = Recycler

    def get_object(self, *args, **kwargs):
        return self.request.user.recycler


class ClientListView(LoginRequiredMixin, ListView):
    template_name = "clients_list_view.html"
    model = Client


class ClientDetailView(LoginRequiredMixin, CurrentUserMixin, DetailView):
    model = Client
    template_name = "clients_detail_view.html"


class AddressDetailView(LoginRequiredMixin, CurrentAddressMixin, DetailView):
    model = Address
    template_name = "address_detail_view.html"


class RecyclerDetailView(LoginRequiredMixin, CurrentRecyclerMixin, DetailView):
    model = Recycler
    template_name = "recycler_detail_view.html"


class ClientUpdateView(LoginRequiredMixin, CurrentUserMixin, UpdateView):
    model = Client
    fields = ["first_name", "last_name", "email", "phone", "strefa"]
    template_name = "form.html"
    success_url = reverse_lazy("base:clients-detail-view")


class AddressUpdateView(LoginRequiredMixin, CurrentAddressMixin, UpdateView):
    model = Address
    fields = ["street", "city", "postal_code"]
    template_name = "form.html"
    success_url = reverse_lazy("base:clients-detail-view")


class RecyclerUpdateView(LoginRequiredMixin, CurrentRecyclerMixin, UpdateView):
    model = Recycler
    fields = [
        "name",
        "street",
        "city",
        "postal_code",
        "nip",
        "available_days",
        "capacity",
        "type",
        "strefa",
    ]
    template_name = "form.html"
    success_url = reverse_lazy("base:recycler-detail-view")


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = "clients_delete.html"
    success_url = reverse_lazy("homepage")


class RecyclerFormView(LoginRequiredMixin, FormView):
    template_name = "recycler.html"
    form_class = RecyclerForm
    success_url = reverse_lazy("base:recycler-detail-view")

    def form_valid(self, form):
        result = super().form_valid(form)
        name = form.cleaned_data["name"]
        street = form.cleaned_data["street"]
        city = form.cleaned_data["city"]
        postal_code = form.cleaned_data["postal_code"]
        nip = form.cleaned_data["nip"]
        available_days = form.cleaned_data["available_days"]
        capacity = form.cleaned_data["capacity"]
        type = form.cleaned_data["type"]
        strefa = form.cleaned_data["strefa"]
        Recycler.objects.create(
            user=self.request.user,
            name=name,
            street=street,
            city=city,
            postal_code=postal_code,
            nip=nip,
            available_days=available_days,
            capacity=capacity,
            type=type,
            strefa=strefa,
        )
        return result

    def form_invalid(self, form):
        return super().form_invalid(form)


class OrderCreateView(LoginRequiredMixin, CreateView):
    form_class = OrderForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.client = self.request.user.client
        form.instance.address = self.request.user.address
        form.instance.user = self.request.user
        form.save()

        choices = {
            "Odpad Elektryczny": "trash:ewastes-create-view",
            "Odpady z Recyklingu": "trash:rwastes-create-view",
            "Niebezpieczne Odpady": "trash:hwastes-create-view",
            "Wielkogabarytowe Odpady": "trash:lswastes-create-view",
        }
        trash = form.cleaned_data["trash_type"]
        return redirect(choices.get(trash))


class OrdersClientList(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders_list.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrdersRecyclerList(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders_recycler_list.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(recycler=self.request.user.recycler)


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "my_order_detail.html"


class OrderRecyclerDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "recycler_order_detail.html"


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = "delete_order.html"
    success_url = reverse_lazy("base:clients-detail-view")


class CheckProfile(LoginRequiredMixin, View):
    def get(self, request):
        if not Client.objects.filter(user=request.user).exists():
            return redirect(reverse("base:clients-form-view"))

        elif not Address.objects.filter(user=request.user).exists():
            return redirect(reverse("base:clients-form-view"))

        return redirect(reverse("base:clients-detail-view"))


class CheckRecycler(LoginRequiredMixin, View):
    def get(self, request):
        if not Recycler.objects.filter(user=self.request.user).exists():
            return redirect(reverse("base:recyclers-form-view"))

        return redirect(reverse("base:recycler-detail-view"))
