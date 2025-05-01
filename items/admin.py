from django.contrib import admin

from items.models import Rarity, Weapon

# Register your models here.


admin.site.register(Weapon)

admin.site.register(Rarity)
