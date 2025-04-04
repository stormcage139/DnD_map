from cgitb import small
from re import T
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
            'Giffs':'Гифы',
            'Forers_Elfs':'Лесные эльфы'}
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
    small_description = models.TextField(blank=True,null=True,verbose_name='Маленькое описание для карточки Без гиперссылок')
    description = models.TextField()
    slug = models.SlugField(max_length=60,unique=True)
    status = models.CharField(max_length=50,null=True,choices=statuses,blank=True)
    population = models.CharField(max_length=50,null=True,choices=race,blank=True)
    npcs = models.ManyToManyField("map.NPC", verbose_name="Ключевые NPC",blank=True)
    what_adventures = models.ManyToManyField("map.Dnd_adventure", verbose_name="В каких приключениях принимал участие",blank=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]
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
    Land = models.ForeignKey(to=Country,on_delete=models.SET_NULL,null=True,related_name="villages",blank=True)
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
    know_npc = models.ManyToManyField("map.NPC", verbose_name=("Каких нпс знает"))
    # adventures = models.ManyToManyField("map.Dnd_adventure", verbose_name=("adventures"),blank=True)
    
    def __str__(self):
        return self.first_name
    
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
        ordering = ["name"]
        verbose_name = "НПС"
        verbose_name_plural = "НПСи"

class Visit(models.Model):
    hero = models.ForeignKey(Hero_m, on_delete=models.CASCADE,related_name='what_visits')
    city = models.ForeignKey(Location, on_delete=models.CASCADE)
    visited_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Посещение ' + self.city.name + ' Героем ' + self.hero.first_name
    class Meta:
        verbose_name = "Посещение"
        verbose_name_plural = "Песещения"
    

class Dnd_adventure(models.Model):
    name = models.CharField(max_length=100,verbose_name='Название приключения')
    number = models.DecimalField(verbose_name='Номер приключения',blank=True,null=True,max_digits=1000,decimal_places=1)
    slug = models.SlugField(null=True,blank=True)
    description = models.TextField(verbose_name='Описание приключения')
    heroes = models.ManyToManyField(to=Hero_m,blank=True,verbose_name='Учавствовашие герои')
    npcs = models.ManyToManyField(to=NPC,blank=True,verbose_name='Учавствовавшие NPCи')
    def __str__(self):
        return str(self.number) + ' ' + self.name

    class Meta:
        ordering=['number']
        verbose_name = "Приключение"
        verbose_name_plural = "Приключения"
    
