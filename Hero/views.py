from re import T
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from map.models import Hero_m,NPC, Dnd_adventure,City,Vilage,Country
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def about_hero_page(request,hero_slug):
    user = Hero_m.objects.get(slug=hero_slug)
    slugs = set([i.slug for i in user.visited_cities.all()])
    cities = City.objects.filter(slug__in=slugs)
    countries = Country.objects.filter(slug__in=slugs)
    villages = Vilage.objects.filter(slug__in=slugs)
    advenures = Dnd_adventure.objects.filter(heroes=user)
    context = {'hero': user,
               'villages':villages,
               'countries':countries,
               'cities':cities,
               'advenures':advenures,
               }
    
    return render(request,'Hero/about_hero.html',context=context)

@login_required
def about_npc_page(request,npc_slug):
    hero = Hero_m.objects.get(username=request.user.username)
    current_npc = NPC.objects.get(slug=npc_slug)
    advenures = Dnd_adventure.objects.filter(npcs=current_npc)
    flag = False
    if request.user.know_npc.filter(slug=npc_slug).exists():
        flag = True
    else:
        flag = False
    if request.user.is_superuser or flag:
        context = {
                'npc': current_npc,
                'advenures':advenures
                }
        return render(request,'Hero/about_npc.html',context=context)
    else:
        return render(request,'map/zaglushka.html')

def login_page(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            HttpResponse('<h1>Неверный логин или пароль</h1>')
    return render(request,'Hero/login.html')

def about_adventure_page(request,adventure_slug):
    adventure = Dnd_adventure.objects.get(slug=adventure_slug)
    context ={'adventure':adventure}
    return render(request,'map/about_adventure.html',context=context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def all_npc(request):
    npcs = NPC.objects.values("name", "slug") 
    context = {'npc_list':npcs}
    return render(request,'hero/all_npc.html',context)