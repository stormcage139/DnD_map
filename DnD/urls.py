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
from django.conf import settings
from django.conf.urls.static import static
from map.admin import Country
from map.views import index, about_Country, about_City_or_Village, authors_page
from Hero.views import about_hero_page, about_npc_page,login_page, user_logout, about_adventure_page,all_npc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', authors_page,name='authors_page'),
    path('', index,name='index'),
    path('login/', login_page,name='login_page'),
    path('logout/', user_logout,name='logout'),
    path('adventure/<slug:adventure_slug>', about_adventure_page,name='adventure_page'),
    path('hero/<slug:hero_slug>/',about_hero_page,name='hero_page'),
    path('all/npc',all_npc,name='npc_page_all'),
    path('all/npc/npc_name=<slug:npc_name>',all_npc,name='npc_page_filtered'),
    path('npc/<slug:npc_slug>/',about_npc_page,name='npc_page'),
    path('location_info/country/<slug:country_slug>/',about_Country,name='country_page'),
    path('location_info/city-or-village/<slug:city_or_village_slug>',about_City_or_Village,name='city_page'),
    # path('location_info/<slug:country_slug>/<slug:vilage_slug>',about_village,name='vilage_page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
