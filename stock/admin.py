from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.site_header = 'Jinesh Infoysis'
admin.site.site_title = 'Stock Manager'
admin.site.unregister(Group)


class LaptopAdmin(admin.ModelAdmin):
    search_fields = ['name', 'keyboard__model_no', 'battery__model_no']
    list_display = ['name', 'battery', 'keyboard']


class BatteryAdmin(admin.ModelAdmin):
    search_fields = ['model_no', ]
    list_display = ['model_no', 'stock', 'code']


class KeyboardAdmin(admin.ModelAdmin):
    search_fields = ['model_no', ]
    list_display = ['model_no', 'stock', 'code']


# Register your models here.
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Battery, BatteryAdmin)
admin.site.register(Keyboard, KeyboardAdmin)
