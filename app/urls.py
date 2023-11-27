from django.contrib import admin
from django.urls import path,include
from home.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('autenticacao.urls')),
    path('evento/',include('evento.urls')),
    path('blog/',include('blog.urls')),
    path('jogo_da_velha',include('jogo_da_velha.urls')),
    path('',home, name='home')
]
