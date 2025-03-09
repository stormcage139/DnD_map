from django.shortcuts import render
from Hero.admin import Hero_m
# Create your views here.

def about_hero_page(request,hero_slug):
    user = Hero_m.objects.get(slug=hero_slug)
    print(user)
    context = {'hero': user}
    return render(request,'Hero/about_hero.html',context=context)