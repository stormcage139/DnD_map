"""
URL configuration for DnD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from map.admin import Country
from map.views import about_village, index, about_Country, about_City
from Hero.views import about_hero_page, about_npc_page,login_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('login/', login_page,name='login_page'),
    path('hero/<slug:hero_slug>/',about_hero_page,name='hero_page'),
    path('npc/<slug:npc_slug>/',about_npc_page,name='npc_page'),
    path('location_info/<slug:country_slug>/',about_Country,name='country_page'),
    path('location_info/<slug:country_slug>/<slug:city_slug>',about_City,name='city_page'),
    path('location_info/<slug:country_slug>/<slug:vilage_slug>',about_village,name='vilage_page'),
]
