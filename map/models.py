from re import T
from tkinter import NO
from django.db import models
from django.contrib.auth.models import AbstractUser


class Location(models.Model):
    race = {'NO':'Нет',
            'Unknown':'Неизвестна',
            'Humans':"Люди",
            'S_elfs':"Высшие эльфы",
            'Gnoms':'Гномы',
            'Dwarfs':'Дварфы',
            'Half_height':'Полурослки',
            'Demons':'Демоны',
            'Drou':"Дроу",
            'Goblins':"Гоблины",
            'Vampires':'Вампиры',
            'Giffs':'Гифы'}
    statuses ={
        "Unknown": "Неизвестен",
        "Martial_law": "Военное положение",
        "Captured": "Захвачен",
        "Resistance": "Сопротивление",
        "Neutral": "Нейтральный",
        "Destroyed": "Уничтожен",
        "Capital": "Столица",
        "Liberal": "Либеральный",
        "Conservative": "Консервативный",
        "Racist": "Расистский"
    }
    image = models.ImageField(upload_to='location_picks/',null=True,blank=True)
    name = models.CharField(max_length=60)
    description = models.TextField()
    slug = models.SlugField(max_length=60,unique=True)
    status = models.CharField(max_length=50,null=True,choices=statuses)
    population = models.CharField(max_length=50,null=True,choices=race)
    npcs = models.ManyToManyField("map.NPC", verbose_name="Ключевые NPC",blank=True)
    what_adventures = models.ManyToManyField("map.Dnd_adventure", verbose_name="В каких приключениях принимал участие",blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Абстрактная модель(не трогай)"
        verbose_name_plural = "Абстрактная модель(не трогай)"
    
class Country(Location):
    glava = models.OneToOneField("map.NPC", verbose_name=("Правитель"), on_delete=models.SET_NULL,null=True,blank=True,default='Неизвестно')
    capital = models.OneToOneField("map.City", verbose_name=("Столица"), on_delete=models.SET_NULL,null=True,related_name="cap_of",blank=True)
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


    
class Vilage(Location):
    glava = models.OneToOneField("map.NPC", verbose_name=("Представитель"), on_delete=models.SET_NULL,null=True,blank=True,default='Неизвестно')
    Land = models.ForeignKey(to=Country,on_delete=models.SET_NULL,null=True,related_name="villages")
    class Meta:
        verbose_name = "Деревня"
        verbose_name_plural = "Деревни"


class City(Location):
    glava = models.OneToOneField("map.NPC", verbose_name=("Мэр"), on_delete=models.SET_NULL,null=True,blank=True,default='Неизвестно')
    Land = models.ForeignKey(to=Country,on_delete=models.SET_NULL,null=True,related_name="cities")


    def is_city(self):
        return True
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"




class Hero_m(AbstractUser):
    email = None
    image = models.ImageField(upload_to='hero_picks/',blank=True)
    visited_cities = models.ManyToManyField(Location, through="Visit",blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=60,unique=True)
    adventures = models.ManyToManyField("map.Dnd_adventure", verbose_name=("adventures"),blank=True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = "Heroes_table"
        verbose_name = "Герой"
        verbose_name_plural = "Герои"

class NPC(models.Model):
    image = models.ImageField(upload_to='npc_picks/',blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "НПС"
        verbose_name_plural = "НПСи"

class Visit(models.Model):
    hero = models.ForeignKey(Hero_m, on_delete=models.CASCADE,related_name='what_visits')
    city = models.ForeignKey(Location, on_delete=models.CASCADE)
    visited_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Посещение ' + self.city.name + ' Героем ' + self.hero.username
    class Meta:
        verbose_name = "Посещение(пока не трогай)"
        verbose_name_plural = "Песещения(пока не трогай)"
    

class Dnd_adventure(models.Model):
    name = models.CharField(max_length=100,verbose_name='Название приключения')
    description = models.TextField(verbose_name='Описание приключения')
    heroes = models.ManyToManyField(to=Hero_m,blank=True,verbose_name='Учавствовашие герои')
    npcs = models.ManyToManyField(to=NPC,blank=True,verbose_name='Учавствовавшие NPCи')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Приключение"
        verbose_name_plural = "Приключения"
    
