from django.shortcuts import render
from map.models import Location,Country,City,Vilage
# Create your views here.


def index(request):
    harinsford = Country.objects.get(slug='harinsford')
    context = {'harinsford':harinsford}
    return render(request,'map/index.html',context=context)    



def about_Country(request,country_slug):
    country = Country.objects.get(slug=country_slug)
    # print(user)
    context = {'location': country}
    return render(request,'map/about_location.html',context=context)

def about_City(request,country_slug,city_slug):
    city_variable = City.objects.get(slug=city_slug)
    # print(user)
    context = {'location': city_variable}
    return render(request,'map/about_location.html',context=context)

def about_Country(request,country_slug):
    country = Country.objects.get(slug=country_slug)
    # print(user)
    context = {'location': country}
    return render(request,'map/about_location.html',context=context)