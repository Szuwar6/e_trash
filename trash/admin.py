from django.contrib import admin

from trash.models import EWaste, RWaste, LSWaste, HWaste


admin.site.register(EWaste)
admin.site.register(RWaste)
admin.site.register(HWaste)
admin.site.register(LSWaste)
