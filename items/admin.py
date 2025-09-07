from django.contrib import admin

from items.models import Rarity, Weapon, Item

# Register your models here.


admin.site.register(Weapon)
admin.site.register(Item)
admin.site.register(Rarity)
