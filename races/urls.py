from django.urls import path
from races.views import all_races,current_race

app_name = "races"

urlpatterns=[
    path("all/",all_races,name="all"),
    path("current/<slug:race_slug>",current_race,name="current")
]