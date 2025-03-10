from django.shortcuts import render
from map.models import Location,Country,City,Vilage,Hero_m
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    harinsford = Country.objects.get(slug='harinsford')
    context = {'harinsford':harinsford}
    return render(request,'map/index.html',context=context)    


@login_required
def about_Country(request,country_slug):
    hero = Hero_m.objects.get(username=request.user.username)
    country = Country.objects.get(slug=country_slug)
    # print(hero.visited_cities.get(slug=country_slug))
    context = {'location': country}
    return render(request,'map/about_location.html',context=context)

@login_required
def about_City(request,country_slug,city_slug):
    city_variable = City.objects.get(slug=city_slug)
    # print(user)
    context = {'location': city_variable}
    return render(request,'map/about_location.html',context=context)


def user_have_access(view_func):
    def wrapper():
        pass