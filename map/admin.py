from django.contrib import admin

from Hero.models import Visit, NPC

from map.models import Location,Country, City, Vilage

# Register your models here.


admin.site.register(Location)

admin.site.register(Visit)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Vilage)
admin.site.register(NPC)