from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import RegexValidator

from trash.models import Trash
from django.contrib.auth.models import User


class Zone(models.Model):
    name = models.CharField("Strefa", max_length=128)

    def __str__(self):
        return f"{self.name}"


class Client(models.Model):
    phone_regex = RegexValidator(
        regex=r"^\d{3}-\d{3}-\d{3}$",
        message="Numer telefonu musi być w formacie 'xxx-xxx-xxx'",
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField("Imię", max_length=128)
    last_name = models.CharField("Nazwisko", max_length=128)
    email = models.EmailField("Adres email")
    phone = models.CharField("Telefon", validators=[phone_regex], max_length=11)
    strefa = models.ForeignKey(
        Zone, on_delete=models.CASCADE, related_name="clients", blank=True, null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Address(models.Model):
    postal_code_regex = RegexValidator(
        regex=r"^\d{2}-\d{3}$", message="Kod pocztowy musi być w formacie 'xx-xxx'"
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    street = models.CharField("Ulica", max_length=128)
    city = models.CharField("Miasto", max_length=128)
    postal_code = models.CharField(
        "Kod pocztowy", validators=[postal_code_regex], max_length=6
    )

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street} {self.city} {self.postal_code}"


class Availability(models.TextChoices):
    MONDAY = (
        "Poniedziałek",
        "Poniedziałek",
    )
    TUESDAY = (
        "Wtorek",
        "Wtorek",
    )
    WEDNESDAY = (
        "Środa",
        "Środa",
    )
    THURSDAY = (
        "Czwartek",
        "Czwartek",
    )
    FRIDAY = (
        "Piątek",
        "Piątek",
    )
    SATURDAY = "Sobota", "Sobota"


day = models.CharField(max_length=15, choices=Availability.choices)


class Recycler(models.Model):
    postal_code_regex = RegexValidator(
        regex=r"^\d{2}-\d{3}$", message="Kod pocztowy musi być w formacie 'xx-xxx'"
    )
    nip_regex = RegexValidator(
        regex=r"^\d{3}-\d{3}-\d{2}-\d{2}$",
        message="NIP musi być w formacie 'xxx-xxx-xx-xx'",
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    CAPACITY_VALUES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    name = models.CharField("Nazwa", max_length=128)
    street = models.CharField("Ulica", max_length=128)
    city = models.CharField("Miasto", max_length=128)
    postal_code = models.CharField(
        "Kod pocztowy", validators=[postal_code_regex], max_length=6
    )
    nip = models.CharField("NIP", validators=[nip_regex], max_length=13)
    available_days = MultiSelectField(
        "Dostępne dni", choices=Availability.choices, default="PN", max_length=128
    )
    capacity = MultiSelectField(
        "Pojemność", choices=CAPACITY_VALUES, max_choices=1, max_length=128, default=1
    )
    type = MultiSelectField("Rodzaj śmieci", choices=Trash.choices, max_length=128)
    strefa = models.ForeignKey(
        Zone, on_delete=models.CASCADE, related_name="recyclers", blank=True, null=True
    )

    def __str__(self):
        return f"{self.name} "


class TimeInterval(models.TextChoices):
    INTERVAL_1 = (
        "8.00 - 10.00",
        "8.00 - 10.00",
    )
    INTERVAL_2 = (
        "10.00 - 12.00",
        "10.00 - 12.00",
    )
    INTERVAL_3 = (
        "12.00 - 14.00",
        "12.00 - 14.00",
    )
    INTERVAL_4 = (
        "14.00 - 16.00",
        "14.00 - 16.00",
    )
    INTERVAL_5 = "16.00 - 18.00", "16.00 - 18.00"


hour = models.CharField(choices=TimeInterval.choices, max_length=32)


class Order(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="orders", null=True
    )
    recycler = models.ForeignKey(
        Recycler, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )
    order_day = models.CharField(
        "Wybierz dzień tygodnia",
        choices=Availability.choices,
        default="PN",
        max_length=15,
    )
    order_time = models.CharField(
        "Wybierz godzinę odbioru",
        choices=TimeInterval.choices,
        default=0,
        max_length=128,
    )
    order_date = models.DateTimeField(auto_now_add=True)
    strefa = models.ForeignKey(
        Zone, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )
    trash_type = models.CharField(
        "Wybierz typ odpadów", choices=Trash.choices, max_length=32
    )

    def __str__(self):
        return f"{self.id}"


class RecyclerAssignedOrders(models.Model):
    recycler = models.ForeignKey(
        Recycler,
        on_delete=models.CASCADE,
        related_name="assigned_orders",
        blank=True,
        null=True,
    )
    order_time = models.ManyToManyField(
        Order, related_name="assigned_orders", blank=True, null=True
    )
