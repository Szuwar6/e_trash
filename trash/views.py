from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
)

from trash.forms import (
    OrderEwasteForm,
    OrderRwasteForm,
    OrderHwasteForm,
    OrderLswasteForm,
)
from trash.models import Trash, EWaste, RWaste, HWaste, LSWaste

User = get_user_model()


class TrashListView(LoginRequiredMixin, ListView):
    template_name = "list_view.html"
    model = Trash


class TrashCreateView(LoginRequiredMixin, CreateView):
    model = Trash
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("trash:ewastes-create-view")


class TrashDetailView(LoginRequiredMixin, DetailView):
    model = Trash
    template_name = "my_trashes.html"


class TrashUpdateView(LoginRequiredMixin, UpdateView):
    model = Trash
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")


class TrashDeleteView(LoginRequiredMixin, DeleteView):
    model = Trash
    template_name = "delete_trash.html"
    success_url = reverse_lazy("homepage")


class EWasteListView(LoginRequiredMixin, ListView):
    model = EWaste
    template_name = "ewastes.html"
    context_object_name = "ewastes"

    def get_queryset(self):
        return EWaste.objects.filter(user=self.request.user)



class EWasteCreateView(LoginRequiredMixin, CreateView):
    model = EWaste
    form_class = OrderEwasteForm
    template_name = "form.html"
    success_url = reverse_lazy("base:clients-detail-view")

    def form_valid(self, form):
        form.instance.client = self.request.user.client
        form.instance.user = self.request.user
        return super().form_valid(form)

class EWasteDetailView(LoginRequiredMixin, DetailView):
    model = EWaste
    template_name = "my_ewastes.html"


class EWasteUpdateView(LoginRequiredMixin, UpdateView):
    model = EWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")


class EWasteDeleteView(LoginRequiredMixin, DeleteView):
    model = EWaste
    template_name = "delete_ewaste.html"
    success_url = reverse_lazy("homepage")


class RWasteListView(LoginRequiredMixin, ListView):
    model = RWaste
    template_name = "rwastes.html"
    context_object_name = "rwastes"

    def get_queryset(self):
        return RWaste.objects.filter(user=self.request.user)


class RWasteCreateView(LoginRequiredMixin, CreateView):
    model = RWaste
    form_class = OrderRwasteForm
    template_name = "form.html"
    success_url = reverse_lazy("base:clients-detail-view")

    def form_valid(self, form):
        form.instance.client = self.request.user.client
        form.instance.user = self.request.user
        return super().form_valid(form)


class RWasteDetailView(LoginRequiredMixin, DetailView):
    model = RWaste
    template_name = "my_rwastes.html"


class RWasteUpdateView(LoginRequiredMixin, UpdateView):
    model = RWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")


class RWasteDeleteView(LoginRequiredMixin, DeleteView):
    model = RWaste
    template_name = "delete_rwaste.html"
    success_url = reverse_lazy("homepage")


class HWasteListView(LoginRequiredMixin, ListView):
    model = HWaste
    template_name = "hwastes.html"
    context_object_name = "hwastes"

    def get_queryset(self):
        return HWaste.objects.filter(user=self.request.user)


class HWasteCreateView(LoginRequiredMixin, CreateView):
    model = HWaste
    form_class = OrderHwasteForm
    template_name = "form.html"
    success_url = reverse_lazy("base:clients-detail-view")

    def form_valid(self, form):
        form.instance.client = self.request.user.client
        form.instance.user = self.request.user
        return super().form_valid(form)


class HWasteDetailView(LoginRequiredMixin, DetailView):
    model = HWaste
    template_name = "my_hwastes.html"


class HWasteUpdateView(LoginRequiredMixin, UpdateView):
    model = HWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")


class HWasteDeleteView(LoginRequiredMixin, DeleteView):
    model = HWaste
    template_name = "delete_hwaste.html"
    success_url = reverse_lazy("homepage")


class LSWasteListView(LoginRequiredMixin, ListView):
    model = LSWaste
    template_name = "lswastes.html"
    context_object_name = "lswastes"

    def get_queryset(self):
        return LSWaste.objects.filter(user=self.request.user)


class LSWasteCreateView(LoginRequiredMixin, CreateView):
    model = LSWaste
    form_class = OrderLswasteForm
    template_name = "form.html"
    success_url = reverse_lazy("base:clients-detail-view")

    def form_valid(self, form):
        form.instance.client = self.request.user.client
        form.instance.user = self.request.user
        return super().form_valid(form)


class LSWasteDetailView(LoginRequiredMixin, DetailView):
    model = LSWaste
    template_name = "my_lswastes.html"


class LSWasteUpdateView(LoginRequiredMixin, UpdateView):
    model = LSWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")


class LSWasteDeleteView(LoginRequiredMixin, DeleteView):
    model = LSWaste
    template_name = "delete_lswaste.html"
    success_url = reverse_lazy("homepage")
