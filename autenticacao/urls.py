from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("logar/",views.logar,name='logar'),
    path("deslogar/",views.deslogar,name='deslogar'),
    path("cadastrar/",views.cadastrar,name='cadastrar'),    
]
