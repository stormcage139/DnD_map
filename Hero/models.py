from django.contrib.auth.models import AbstractUser
from django.db import models


class HeroModel(AbstractUser):
    image = models.ImageField(upload_to='hero_picks/',blank=True)
    visited_cities = models.ManyToManyField("map.Location", through="Visit",blank=True)
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


class Visit(models.Model):
    hero = models.ForeignKey(HeroModel, on_delete=models.CASCADE, related_name='what_visits')
    city = models.ForeignKey("map.Location", on_delete=models.CASCADE)
    visited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Посещение ' + self.city.name + ' Героем ' + self.hero.first_name

    class Meta:
        verbose_name = "Посещение"
        verbose_name_plural = "Песещения"


