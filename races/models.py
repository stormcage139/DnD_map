from django.db import models

class Race(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    race_slug = models.SlugField(max_length=40,unique=True,blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Раса"
        verbose_name_plural = "Расы"
