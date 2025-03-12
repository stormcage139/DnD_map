from http.client import HTTPResponse
from tkinter import NO
from urllib.request import HTTPRedirectHandler
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from map.models import Location,Country,City,Vilage,Hero_m
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    context = {}
    for country in Country.objects.all():
        context[country.slug] = country
    context['heroes'] = Hero_m.objects.all()

    # harinsford = Country.objects.get(slug='harinsford')
    # cantov_hills = Country.objects.get(slug='cantov_hills')
    # edliada_forest = Country.objects.get(slug='edliada_forest')
    # helmogros = Country.objects.get(slug='helmogros')
    # flaoorn = Country.objects.get(slug='flaoorn')
    # alftand = Country.objects.get(slug='alftand')
    # vampire_lands = Country.objects.get(slug='vampire_lands')
    # vruveriat = Country.objects.get(slug='vruveriat')
    # gornor = Country.objects.get(slug='gornor')
    # delackort = Country.objects.get(slug='delackort')
    # harinsford = Country.objects.get(slug='harinsford')
    # harinsford = Country.objects.get(slug='harinsford')
    # harinsford = Country.objects.get(slug='harinsford')
    # context = {'harinsford':harinsford,
    #            'cantov_hills':cantov_hills,
    #            'edliada_forest':edliada_forest,
    #            'helmogros': helmogros,
    #            'flaoorn':   flaoorn,
    #         #    отсуда добавлять
    #            'alftand':alftand,
    #            'vampire_lands':vampire_lands,
    #            'vruveriat' :vruveriat,
    #            'gornor':gornor,
    #            'delackort':delackort,
    #            'harinsford':harinsford,
    #            'heroes': Hero_m.objects.all()}
    
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