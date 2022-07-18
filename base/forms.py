# jeżeli użytkownik wybiera datę i godzinę to filtrowana jest lista recyclerów, którzy są dostępni w danym terminie
#
# Dostępni w danym terminie to znaczy, że w danym przedziale czasowym ilość zamówień przypisanych do recyclera nie przekracza capacity
#
# recycler agregate count orders po tym będziemy filtrować -> count orders w danej godzinie
#
# Potem z tej listy recyclerów możemy zrobić random albo first i przekażemy go do order objects create

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


# FORMULARZE CLIENT

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


# FORMULARZE RECYCLER

class RecyclerForm(Form):
    user = forms.ModelChoiceField(widget=forms.HiddenInput(), required=False, queryset=None)
    name = CharField(max_length=128, label="Nazwa firmy:")
    street = CharField(max_length=128, label="Adres firmy:")
    city = CharField(max_length=128, label="Miasto:")
    postal_code = CharField(max_length=128, label="Kod pocztowy:")
    nip = CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], label="Numer NIP:")
    available_days = MultipleChoiceField(choices=Availability.choices,
                                         label="Dostępne dni odbiorów w godz. 8.00 - 18.00:")
    capacity = ChoiceField(choices=Recycler.CAPACITY_VALUES,
                           label="Ilość klientów możliwa do obsłużenia w ciągu 2 godzin:")
    type = MultipleChoiceField(choices=Trash.choices, label="Rodzaje odbieranych odpadów:")
    zone = ModelChoiceField(queryset=Zone.objects.all(), label="Strefy odbioru odpadów:")

    # def clean(self):
    #     result = super().clean()
    #     if not self.errors:
    #         if result['name'][0].islower:
    #             raise ValidationError(
    #                 "Nazwa firmy musi zaczynać się z dużej litery."
    #             )
    #     return result




# FORMULARZE ORDER

# def order_numeration_validator(value):
#     value = Order.order_number
#     format_value = f'ORD{Order.id}/2022'
#     return value


def order_day_choice(value):
    value = Order.order_day
    available_recyclers = Recycler.objects.filter(available_days=value)
    if value in available_recyclers:
        Order.objects.create()
    else:
        raise ValidationError(
            "Brak dostępnych odbiorców w wybranym terminie, prosimy o wybranie innego dnia"
        )


def order_time_choice(value):
    value = Order.order_time
    assigned_orders = RecyclerAssignedOrders.objects.aggregate(Count('order_time'))
    capacity = Recycler.objects.filter('capacity')
    if value:
        if assigned_orders <= capacity:
            Order.objects.create()
        else:
            raise ValidationError(
                "Brak dostępnych odbiorców w wybranych godzinach, prosimy o wybranie innego terminu"
            )


class OrderForm(forms.ModelForm):
    client = forms.ModelChoiceField(widget=forms.HiddenInput(), required=False, queryset=None)
    # order_number = forms.ModelChoiceField(widget=forms.HiddenInput(), required=False, queryset=None)

    class Meta:
        model = Order
        fields = ['id','order_number', 'order_day', 'order_time', 'strefa', 'adres', 'trash_type', 'client']


# POPRZEDNIA WERSJA FORMULARZA Order
#Zostawiona na wszelki wypadek

# class OrderNumberField(CharField):
#     def order_numeration(self, value):
#         value = f'ORD{Order.id}/2022'
#         return value


# class OrderDateField(ChoiceField):
#     def order_day_choice(self, value):
#         available_recyclers = Recycler.objects.filter(available_days=value)
#         if value in available_recyclers:
#             Order.objects.create()
#         else:
#             raise ValidationError(
#                 "Brak dostępnych odbiorców w wybranym terminie, prosimy o wybranie innego dnia"
#             )


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
