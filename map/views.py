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
    for village in Vilage.objects.all():
        context[village.slug] = village
    context['heroes'] = Hero_m.objects.all()
    context['adventures'] = Dnd_adventure.objects.all() 
    return render(request,'map/index.html',context=context)    


@login_required
def about_Country(request,country_slug):
    hero = Hero_m.objects.get(username=request.user.username)
    country = Country.objects.get(slug=country_slug)
    context = {'location': country}
    if not request.user.is_superuser:
        was_here_or_not = hero.what_visits.filter(city__slug=country_slug)
        if not was_here_or_not.exists():
            return render(request,'map/zaglushka.html')
        return render(request,'map/about_location.html',context=context)
    else:
       return render(request,'map/about_location.html',context=context)


@login_required
def about_City_or_Village(request,city_or_village_slug):
    print("Kapusta")
    hero = Hero_m.objects.get(username=request.user.username)
    city_or_village_variable = City.objects.filter(slug=city_or_village_slug)
    if city_or_village_variable.exists():
        city_or_village_variable = city_or_village_variable.get()
    else:
        city_or_village_variable = Vilage.objects.filter(slug=city_or_village_slug).get()
    if not request.user.is_superuser:
            was_here_or_not = hero.what_visits.filter(city__slug=city_or_village_variable.slug)
            if not was_here_or_not.exists():
                 return render(request,'map/zaglushka.html')
            else:
                context = {'location': city_or_village_variable}   
                return render(request,'map/about_location.html',context=context)
    else:
        context = {'location': city_or_village_variable}   
        return render(request,'map/about_location.html',context=context)

def authors_page(request):
    return render(request,'map/authors.html')
# @login_required
# def about_village(request,country_slug,village_slug):
#     village_variable = Vilage.objects.get(slug=village_slug)
#     # print(user)
#     context = {'location': village_variable}
#     return render(request,'map/about_location.html',context=context)

def user_have_access(view_func) :
    def wrapper():
        pass