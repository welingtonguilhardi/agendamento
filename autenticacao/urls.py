from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("logar/",views.logar),
    path("deslogar/",views.deslogar),
    path("cadastrar/",views.cadastro),    
]
