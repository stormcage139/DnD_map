from django.db import models


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
    npcs = models.ManyToManyField("Hero.NPC", verbose_name="Ключевые NPC",blank=True)
    what_adventures = models.ManyToManyField("adventures.DndAdventure", verbose_name="В каких приключениях принимал участие",blank=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]
        verbose_name = "Абстрактная модель(не трогай)"
        verbose_name_plural = "Абстрактная модель(не трогай)"
    
class Country(Location):
    glava = models.OneToOneField("Hero.NPC", verbose_name=("Правитель"), on_delete=models.SET_NULL,null=True,blank=True,default='Неизвестно')
    capital = models.OneToOneField("map.City", verbose_name=("Столица"), on_delete=models.SET_NULL,null=True,related_name="cap_of",blank=True)
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


    
class Vilage(Location):
    glava = models.OneToOneField("Hero.NPC", verbose_name=("Представитель"), on_delete=models.SET_NULL,null=True,blank=True,default='Неизвестно')
    Land = models.ForeignKey(to="map.Country",on_delete=models.SET_NULL,null=True,related_name="villages",blank=True)
    class Meta:
        verbose_name = "Деревня"
        verbose_name_plural = "Деревни"


class City(Location):
    glava = models.OneToOneField("Hero.NPC", verbose_name=("Мэр"), on_delete=models.SET_NULL,null=True,blank=True,default='Неизвестно')
    Land = models.ForeignKey(to="map.Country",on_delete=models.SET_NULL,null=True,related_name="cities")


    def is_city(self):
        return True
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"







