from django.contrib import admin
from apps.search.models import Airport, Flight


class AirportAdmin(admin.ModelAdmin):
    list_display = ('iataCode', 'name')
    search_fields = ['iataCode', 'name']


class FlightAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'flightNum', 'fromDate', 'toDate', 'ska', 'skd')
    search_fields = ['origin', 'destination']


admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
