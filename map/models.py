from django.db import models
from django.contrib.auth.models import AbstractUser


class Location(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    slug = models.CharField(max_length=30)

    def __str__(self):
        return 'Имя героя' + self.name
    
class Hero_m(AbstractUser):
    image = models.ImageField(upload_to='hero_picks/')
    visited_cities = models.ManyToManyField(Location, through="Visit")
    
    def __str__(self):
        return 'Имя героя ' + self.username
    
    class Meta:
        db_table = "Heroes_table"
    
class Visit(models.Model):
    hero = models.ForeignKey(Hero_m, on_delete=models.CASCADE)
    city = models.ForeignKey(Location, on_delete=models.CASCADE)
    visited_at = models.DateTimeField(auto_now_add=True)
