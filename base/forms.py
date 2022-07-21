from datetime import datetime

from django import forms
from django.core.validators import RegexValidator
from django.db.models import Count
from django.forms import CharField, Form, ModelForm, ModelChoiceField, MultipleChoiceField, ChoiceField
from django.core.exceptions import ValidationError

# import pytz

from base.models import Client, Address, Recycler, Order, Availability, Zone, RecyclerAssignedOrders, TimeInterval

# utc = pytz.UTC
from trash.models import Trash


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


class ClientForm(ModelForm):
    user = forms.ModelChoiceField(widget=forms.HiddenInput(), required=False, queryset=None)

    class Meta:
        model = Client
        fields = "__all__"


class AddressForm(ModelForm):
    user = forms.ModelChoiceField(widget=forms.HiddenInput(), required=False, queryset=None)

    class Meta:
        model = Address
        fields = "__all__"


class RecyclerForm(forms.ModelForm):
    user = forms.ModelChoiceField(widget=forms.HiddenInput(), required=False, queryset=None)

    class Meta:
        model = Recycler
        fields = "__all__"


# def order_numeration_validator(value):
#     value = Order.order_number
#     format_value = f'ORD{Order.id}/2022'
#     return value


# def order_day_choice(value):
#     value = Order.order_day
#     available_recyclers = Recycler.objects.filter(available_days=value)
#     if value in available_recyclers:
#         Order.objects.create()
#     else:
#         raise ValidationError(
#             "Brak dostępnych odbiorców w wybranym terminie, prosimy o wybranie innego dnia"
#         )
#
#
# def order_time_choice(value):
#     value = Order.order_time
#     assigned_orders = RecyclerAssignedOrders.objects.aggregate(Count('order_time'))
#     capacity = Recycler.objects.filter('capacity')
#     if value:
#         if assigned_orders <= capacity:
#             Order.objects.create()
#         else:
#             raise ValidationError(
#                 "Brak dostępnych odbiorców w wybranych godzinach, prosimy o wybranie innego terminu"
#             )
#
#
#
# class OrderDateField(ChoiceField):
#     def order_day_choice(self, value):
#         available_recyclers = Recycler.objects.filter(available_days=value)
#         if value in available_recyclers:
#             Order.objects.create()
#         else:
#             raise ValidationError(
#                 "Brak dostępnych odbiorców w wybranym terminie, prosimy o wybranie innego dnia"
#             )
#
#
# class OrderTimeField(ChoiceField):
#     def order_time_choice(self, capacity):
#         assigned_orders = RecyclerAssignedOrders.objects.aggregate(Count('order_time'))
#         capacity = Recycler.objects.filter('capacity')
#         if assigned_orders <= capacity:
#             Order.objects.create()
#         else:
#             raise ValidationError(
#                 "Brak dostępnych odbiorców w wybranych godzinach, prosimy o wybranie innego terminu"
#             )


class OrderForm(forms.ModelForm):
    client = forms.ModelChoiceField(widget=forms.HiddenInput(), required=False, queryset=None)
    address = forms.ModelChoiceField(widget=forms.HiddenInput(), required=False, queryset=None)

    class Meta:
        model = Order
        fields = ['id', 'recycler', 'order_day', 'order_time', 'strefa', 'address', 'trash_type', 'client']

# POPRZEDNIA WERSJA FORMULARZA Order
# Zostawiona na wszelki wypadek

# class OrderNumberField(CharField):
#     def order_numeration(self, value):
#         value = f'ORD{Order.id}/2022'
#         return value


# class OrderForm(Form):
#     order_number = OrderNumberField(max_length=128, label="Numer zamówienia:")
#     order_day = OrderDateField(choices=Availability.choices, label= "Wybierz dzień odbioru odpadów:")
#     order_time = OrderTimeField(choices=TimeInterval.choices, label= "Wybierz godzinę odbioru odpadów:")
#     # order_date = DateTimeField()#tu chcę automatycznie dodającą się aktualną datę
#     zone = ModelChoiceField(queryset=Zone.objects.all(), label="Strefy odbioru odpadów:")
#     address = ModelChoiceField(queryset=Address.objects.all(), label="Adres odbioru:")
#     # city = CharField(max_length=128, label="Miasto:")
#     # postal_code= CharField(max_length=128, label="Kod pocztowy:")
#     trash_type = MultipleChoiceField(choices=Trash.choices, label="Rodzaj odpadów:")
