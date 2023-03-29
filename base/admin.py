from django.contrib import admin

# Register your models here.
from base.models import Client, Recycler, Zone, Address, Order

admin.site.register(Client)
admin.site.register(Recycler)
admin.site.register(Zone)
admin.site.register(Address)
admin.site.register(Order)
