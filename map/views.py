from http.client import HTTPResponse
from tkinter import NO
from urllib.request import HTTPRedirectHandler
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from map.models import Location,Country,City,Vilage,Hero_m, Dnd_adventure
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    context = {}
    for country in Country.objects.all():
        context[country.slug] = country
    for city in City.objects.all():
        context[city.slug] = city
    context['heroes'] = Hero_m.objects.all()
    context['adventures'] = Dnd_adventure.objects.all() 
    return render(request,'map/index.html',context=context)    


@login_required
def about_Country(request,country_slug):
    hero = Hero_m.objects.get(username=request.user.username)
    country = Country.objects.get(slug=country_slug)
    context = {'location': country}
    # print(country)
    if not request.user.is_superuser:
        try:
            was_here_or_not = hero.what_visits.get(city__slug=country_slug)
        except Exception:
            was_here_or_not = None
        if was_here_or_not != None:
            return render(request,'map/about_location.html',context=context)
        else:
            return HttpResponse("<h1>У вас не доступа к информации об этой локации</h1>")
    else:
       return render(request,'map/about_location.html',context=context)


@login_required
def about_City_or_Village(request,country_slug,city_or_village_slug):
    try:
        city_or_village_variable = City.objects.filter(slug=city_or_village_slug)
        if city_or_village_variable.exists():
            city_or_village_variable = city_or_village_variable.get()
        else:
            city_or_village_variable = Vilage.objects.filter(slug=city_or_village_slug).get()
    except Exception:
        city_or_village_variable = None
    context = {'location': city_or_village_variable}
    return render(request,'map/about_location.html',context=context)

# @login_required
# def about_village(request,country_slug,village_slug):
#     village_variable = Vilage.objects.get(slug=village_slug)
#     # print(user)
#     context = {'location': village_variable}
#     return render(request,'map/about_location.html',context=context)

def user_have_access(view_func) :
    def wrapper():
        pass