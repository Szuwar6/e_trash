from django.db import models

from trash.models import Trash
from django.contrib.auth.models import User


class Zone(models.Model):
    name = models.CharField("Strefa", max_length=128)

    def __str__(self):
        return f"{self.name}"


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField("Imię", max_length=128)
    last_name = models.CharField("Nazwisko", max_length=128)
    email = models.CharField("Adres email", max_length=128) #walidacja
    phone = models.IntegerField("Telefon", max_length=9) #walidacja przedrostek
    strefa = models.ForeignKey(
        Zone, on_delete=models.CASCADE, related_name="clients", blank=True, null=True
     )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Address(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="addresses", blank=True, null=True
    )
    street = models.CharField("Ulica", max_length=128)
    city = models.CharField("Miasto", max_length=128)
    postal_code = models.PositiveSmallIntegerField("Kod pocztowy", max_length=5)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street} {self.city} {self.postal_code}"


class Availability(models.TextChoices):
    MONDAY = 'Poniedziałek', 'Poniedziałek',
    TUESDAY = 'Wtorek', 'Wtorek',
    WEDNESDAY = 'Środa', 'Środa',
    THURSDAY = 'Czwartek', 'Czwartek',
    FRIDAY = 'Piątek', 'Piątek',
    SATURDAY = 'Sobota', 'Sobota'
day = models.CharField(max_length=15, choices=Availability.choices)


class Recycler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    CAPACITY_VALUES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
    name = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postal_code = models.PositiveSmallIntegerField(max_length=5)
    nip = models.IntegerField(max_length=10)
    available_days = models.CharField(choices=Availability.choices, default='PN', max_length=15)
    capacity = models.SmallIntegerField(choices=CAPACITY_VALUES, max_length=1, default='1')
    type = models.CharField(choices=Trash.choices, max_length=32)
    zone = models.ForeignKey(
        Zone, on_delete=models.CASCADE, related_name="recyclers", blank=True, null=True
    )
    def __str__(self):
        return f"{self.name} "

class TimeInterval(models.TextChoices):
    INTERVAL_1 = '8.00 - 10.00', '8.00 - 10.00',
    INTERVAL_2 = '10.00 - 12.00', '10.00 - 12.00',
    INTERVAL_3 = '12.00 - 14.00', '12.00 - 14.00',
    INTERVAL_4 = '14.00 - 16.00', '14.00 - 16.00',
    INTERVAL_5 = '16.00 - 18.00', '16.00 - 18.00'

hour = models.CharField(choices=TimeInterval.choices, max_length=32)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders', null=True)
    recycler = models.ForeignKey(
        Recycler, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )
    order_number = models.CharField("Numer zamówienia", auto_created=True, max_length=14)
    order_day = models.CharField("Wybierz dzień tygodnia", choices=Availability.choices, default='PN', max_length=15)
    order_time = models.CharField("Wybierz godzinę odbioru", choices=TimeInterval.choices, default=0, max_length=128)
    order_date = models.DateTimeField(auto_now_add=True)
    strefa = models.ForeignKey(
        Zone, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )
    adres = models.ForeignKey(
        Address, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )
    trash_type = models.CharField("Wybierz typ odpadów", choices=Trash.choices, max_length=32)

    def __str__(self):
        return f"{self.order_number}"


class RecyclerAssignedOrders(models.Model):
    recycler = models.ForeignKey(
        Recycler, on_delete=models.CASCADE, related_name="assigned_orders", blank=True, null=True
    )
    order_time = models.ManyToManyField(
        Order, related_name="assigned_orders", blank=True, null=True
    )

