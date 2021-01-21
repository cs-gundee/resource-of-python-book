from django.contrib import admin

from .models import Center, Transport, Passenger

class TransportAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "distance")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("transports",)

# Register your models here.
admin.site.register(Center)
admin.site.register(Transport, TransportAdmin)
admin.site.register(Passenger, PassengerAdmin)