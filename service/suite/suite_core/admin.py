from django.contrib import admin
from suite_core.models import RoomAvailable
from suite_core.models import Service
from suite_core.models import Modifier
from suite_core.models import PriceList

class RoomAvailableAdmin (admin.ModelAdmin):
    list_display = ('number', 'room_type')

class ServiceAdmin (admin.ModelAdmin):
    list_display = ('name',)

class ModifierAdmin (admin.ModelAdmin):
    list_display = ('name', 'amount', 'perc')

class PriceListAdmin (admin.ModelAdmin):
    list_display = ('name', 'service', 'date_start', 'date_end', 'price')

admin.site.register (RoomAvailable, RoomAvailableAdmin)
admin.site.register (Service, ServiceAdmin)
admin.site.register (Modifier, ModifierAdmin)
admin.site.register (PriceList, PriceListAdmin)
