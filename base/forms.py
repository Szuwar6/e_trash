from django import forms

from django.forms import ModelForm

from base.models import Client, Address, Recycler, Order


class ClientForm(ModelForm):
    user = forms.ModelChoiceField(
        widget=forms.HiddenInput(), required=False, queryset=None
    )

    class Meta:
        model = Client
        fields = "__all__"


class AddressForm(ModelForm):
    user = forms.ModelChoiceField(
        widget=forms.HiddenInput(), required=False, queryset=None
    )

    class Meta:
        model = Address
        fields = "__all__"


class RecyclerForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        widget=forms.HiddenInput(), required=False, queryset=None
    )

    class Meta:
        model = Recycler
        fields = "__all__"


class OrderForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        widget=forms.HiddenInput(), required=False, queryset=None
    )
    address = forms.ModelChoiceField(
        widget=forms.HiddenInput(), required=False, queryset=None
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "recycler",
            "order_day",
            "order_time",
            "strefa",
            "address",
            "trash_type",
            "client",
        ]
