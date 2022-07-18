from django.contrib.auth.models import User
from django.db import models




class Trash(models.TextChoices):
    ELECTRICAL = 'Odpad Elektryczny', 'Odpad Elektryczny',
    RECYCLED = 'Odpady z Recyklingu', 'Odpady z Recyklingu',
    HAZARDOUS = 'Niebezpieczne Odpady', 'Niebezpieczne Odpady',
    LARGE = 'Wielkogabarytowe Odpady', 'Wielkogabarytowe Odpady'


type = models.CharField(choices=Trash.choices, max_length=32)


class Meta:
    verbose_name_plural = "Trashes"


def __str__(self):
    return f"{self.type}"


class EWaste(models.Model):
    EWASTES = [('Zmywarka', 'Zmywarka'), ('TV', 'TV'), ('Laptop', 'Laptop'), ('Pralka', 'Pralka'), ('Lodówka', 'Lodówka'),
               ('Monitor', 'Monitor'), ('Mikrofalówka', 'Mikrofalówka'), ('Odkurzacz', 'Odkurzacz'), ('Kuchenka', 'Kuchenka'),
               ('Piekarnik', 'Piekarnik'), ('Inne', 'Inne')]
    client = models.ForeignKey(
        'base.Client', on_delete=models.CASCADE, related_name="ewastes", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='ewastes', null=True)
    type = models.CharField('Wybierz rodzaj odpadów:', choices=EWASTES, max_length=20)
    height = models.PositiveSmallIntegerField('Wysokość:', max_length=5)
    width = models.PositiveSmallIntegerField('Szerokość:', max_length=5)
    length = models.PositiveSmallIntegerField('Długość:', max_length=5)
    weight = models.PositiveSmallIntegerField('Waga:', max_length=5)

    def __str__(self):
        return f"{self.type}"


class RWaste(models.Model):
    RWASTES = [('Papier', 'Papier'), ('Plastik', 'Plastik'), ('Szkło', 'Szkło'), ('BIO', 'BIO')]
    client = models.ForeignKey(
        'base.Client', on_delete=models.CASCADE, related_name="rwastes", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='rwastes', null=True)
    type = models.CharField('Wybierz rodzaj odpadów:', choices=RWASTES, max_length=10)
    trash_amount = models.PositiveSmallIntegerField('Pojemność worków(l)', max_length=5)

    def __str__(self):
        return f"{self.type}"


class HWaste(models.Model):
    HWASTES = [('Farby', 'Farby'), ('Oleje', 'Oleje'), ('Leki', 'Leki'), ('Baterie', 'Baterie'), ('Żarówki', 'Żarówki'),
               ('Tonery', 'Tonery'), ('Inne', 'Inne')]
    client = models.ForeignKey(
        'base.Client', on_delete=models.CASCADE, related_name="hwastes", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='hwastes', null=True)
    type = models.CharField('Odpad', choices=HWASTES, max_length=10)
    trash_amount = models.PositiveSmallIntegerField('Ilość(l/kg/szt)', max_length=5)

    def __str__(self):
        return f"{self.type}"


class LSWaste(models.Model):
    LSWASTES = [('Szafa', 'Szafa'), ('Fotel', 'Fotel'), ('Kanapa', 'Kanapa'), ('Stół', 'Stół'), ('Wanna', 'Wanna'),
                ('Komoda', 'Komoda'), ('Umywalka', 'Umywalka'), ('Łóżko', 'Łóżko'), ('Inne' , 'Inne')]
    client = models.ForeignKey(
        'base.Client', on_delete=models.CASCADE, related_name="lswastes", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='lswastes', null=True)
    type = models.CharField('Wybierz rodzaj odpadów:', choices=LSWASTES, max_length=10)
    height = models.PositiveSmallIntegerField('Wysokość:', max_length=5)
    width = models.PositiveSmallIntegerField('Szerokość:', max_length=5)
    length = models.PositiveSmallIntegerField('Długość:', max_length=5)
    weight = models.PositiveSmallIntegerField('Waga:', max_length=5)

    def __str__(self):
        return f"{self.type}"
