from django.shortcuts import render, HttpResponseRedirect
from map.models import Hero_m,NPC
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def about_hero_page(request,hero_slug):
    user = Hero_m.objects.get(slug=hero_slug)
    context = {'hero': user}
    return render(request,'Hero/about_hero.html',context=context)

def about_npc_page(request,npc_slug):
    current_npc = NPC.objects.get(slug=npc_slug)
    context = {'npc': current_npc}
    return render(request,'Hero/about_npc.html',context=context)

def login_page(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
    return render(request,'Hero/login.html')