from django.db import models
from django.urls import reverse

from map.models import Hero_m, Dnd_adventure


# Create your models here.
class Review(models.Model):
    review_text = models.TextField(verbose_name="Текст рецензии")
    event = models.OneToOneField(Dnd_adventure,verbose_name=("Приключение"), on_delete=models.CASCADE)
    reviewer = models.OneToOneField(Hero_m,verbose_name=("Автор"), related_name="as_review",on_delete=models.CASCADE)


    def __str__(self):
        return f"Отзыв {self.reviewer} о приключении {self.event}"

    def get_absolute_url(self):
        return reverse('reviews:cur_review_page', kwargs={"review_id": self.id})
        


