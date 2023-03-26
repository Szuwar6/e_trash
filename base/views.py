from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from django.views.generic import (

    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    FormView,
)

from base.forms import ClientForm, AddressForm, RecyclerForm, OrderForm
from base.models import Client, Address, Recycler, Order


@login_required
def client_address_create(request):
    form = ClientForm(request.POST or None)
    form_2 = AddressForm(request.POST or None)
    if all([form.is_valid(), form_2.is_valid()]):
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        phone = form.cleaned_data["phone"]
        strefa = form.cleaned_data["strefa"]
        street = form_2.cleaned_data["street"]
        city = form_2.cleaned_data["city"]
        postal_code = form_2.cleaned_data["postal_code"]
        client = Client.objects.create(
            user=request.user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            strefa=strefa,
        )
        Address.objects.create(
            user=request.user, street=street, city=city, postal_code=postal_code
        )
        return redirect(reverse("base:clients-detail-view"))
    return render(
        request,
        template_name="client_address.html",
        context={"form": form, "form_2": form_2},
    )


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


@login_required
def order_user(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.instance.client = request.user.client
            form.instance.address = request.user.address
            form.instance.user = request.user
            form.save()
            trash = form.cleaned_data["trash_type"]
            if trash == "Odpad Elektryczny":
                return redirect(reverse("trash:ewastes-create-view"))
            elif trash == "Odpady z Recyklingu":
                return redirect(reverse("trash:rwastes-create-view"))
            elif trash == "Niebezpieczne Odpady":
                return redirect(reverse("trash:hwastes-create-view"))
            elif trash == "Wielkogabarytowe Odpady":
                return redirect(reverse("trash:lswastes-create-view"))

    else:
        form = OrderForm
    return render(request, "form.html", {"form": form})


@login_required
def orders_list(request):
    return render(
        request,
        template_name="orders_list.html",
        context={"orders": Order.objects.filter(user=request.user)},
    )




def orders_recycler_list(request):
    return render(
        request,
        template_name="orders_recycler_list.html",
        context={"orders": Order.objects.filter(recycler=request.user.recycler)},
    )


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



@login_required
def check_profile(request):
    if not Client.objects.filter(user=request.user).exists():
        return redirect(reverse("base:clients-form-view"))

    if not Address.objects.filter(user=request.user).exists():
        return redirect(reverse("base:clients-form-view"))

    return redirect(reverse("base:clients-detail-view"))


@login_required
def check_recycler(request):
    if not Recycler.objects.filter(user=request.user).exists():
        return redirect(reverse("base:recyclers-form-view"))

    return redirect(reverse("base:recycler-detail-view"))
