# Generated by Django 4.1.3 on 2023-01-03 19:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_client_email_alter_client_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message="Numer telefonu musi być w formacie 'xxx-xxx-xxx'", regex='^\\d{3}-\\d{3}-\\d{3}$')], verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='recycler',
            name='nip',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="NIP musi być w formacie 'xxx-xxx-xx-xx'", regex='^\\d{3}-\\d{3}-\\d{2}-\\d{2}$')], verbose_name='NIP'),
        ),
    ]