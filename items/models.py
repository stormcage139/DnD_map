# -*- coding: utf-8 -*-


from django.db import models

class Rarity(models.Model):

    name = models.CharField(max_length=50)
    level = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Редкость"
        verbose_name_plural = "Редкости"

class Item(models.Model):
    name = models.CharField(max_length=150,null=False)
    description = models.TextField(null=True)
    rarity = models.ForeignKey(to=Rarity,on_delete=models.SET_DEFAULT,default=None)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"


class Weapon(Item):
    damage = models.PositiveSmallIntegerField(null=True)

    class Meta:
        verbose_name = "Оружие"
        verbose_name_plural = "Оружия"

    


