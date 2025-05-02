from django.contrib import admin

from Hero.models import Visit

from map.models import Location,Country, City, Vilage,NPC

# Register your models here.


admin.site.register(Location)

admin.site.register(Visit)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Vilage)
admin.site.register(NPC)