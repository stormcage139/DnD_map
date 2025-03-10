from django.shortcuts import render
from map.models import Hero_m,NPC
# Create your views here.

def about_hero_page(request,hero_slug):
    user = Hero_m.objects.get(slug=hero_slug)
    context = {'hero': user}
    return render(request,'Hero/about_hero.html',context=context)

def about_npc_page(request,npc_slug):
    current_npc = NPC.objects.get(slug=npc_slug)
    context = {'npc': current_npc}
    return render(request,'Hero/about_npc.html',context=context)