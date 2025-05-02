from django.db import models

from Hero.models import HeroModel, NPC


# Create your models here.
class DndAdventure(models.Model):
    name = models.CharField(max_length=100,verbose_name='Название приключения')
    number = models.DecimalField(verbose_name='Номер приключения',blank=True,null=True,max_digits=1000,decimal_places=1)
    slug = models.SlugField(null=True,blank=True)
    description = models.TextField(verbose_name='Описание приключения')
    heroes = models.ManyToManyField(to=HeroModel,blank=True,verbose_name='Учавствовашие герои')
    npcs = models.ManyToManyField(to=NPC,blank=True,verbose_name='Учавствовавшие NPCи')
    def __str__(self):
        return str(self.number) + ' ' + self.name

    class Meta:
        ordering=['number']
        verbose_name = "Приключение"
        verbose_name_plural = "Приключения"
