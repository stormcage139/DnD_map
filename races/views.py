from django.shortcuts import render

# Create your views here.
def all_races(request):
    return render(request,"races/all.html")

def current_race(request,race_slug):
    return render(request,"races/current_race.html")