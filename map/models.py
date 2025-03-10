from django.db import models
from django.contrib.auth.models import AbstractUser


class Location(models.Model):

    name = models.CharField(max_length=60)
    description = models.TextField()
    slug = models.SlugField(max_length=60,unique=True)
    status = models.CharField(max_length=50,null=True)
    population = models.CharField(max_length=50)
    npsc = models.ManyToManyField("map.NPC", verbose_name="where_was")

    def __str__(self):
        return self.name
    
class Country(Location):
    pass

class Vilage(Location):
    Land = models.ForeignKey(to=Country,on_delete=models.SET_NULL,null=True,related_name="villages")
    pass

class City(Location):
    Land = models.ForeignKey(to=Country,on_delete=models.SET_NULL,null=True,related_name="cities")
    pass



class Hero_m(AbstractUser):
    image = models.ImageField(upload_to='hero_picks/')
    visited_cities = models.ManyToManyField(Location, through="Visit")
    description = models.TextField()
    slug = models.SlugField(max_length=60)
    adventures = models.ForeignKey(to="map.Dnd_adventure", verbose_name="heroes", on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = "Heroes_table"

class NPC(models.Model):
    name = models.CharField( max_length=50)
    description = models.TextField()
    adventures = models.ForeignKey(to="map.Dnd_adventure", verbose_name="what_adventure", on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Visit(models.Model):
    hero = models.ForeignKey(Hero_m, on_delete=models.CASCADE)
    city = models.ForeignKey(Location, on_delete=models.CASCADE)
    visited_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Посещение ' + self.city.name + ' Героем ' + self.hero.username
    

class Dnd_adventure(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    heroes = models.ManyToManyField(to=Hero_m,blank=True)
    npcs = models.ManyToManyField(to=NPC,blank=True)
    
    def __str__(self):
        return self.name
    
