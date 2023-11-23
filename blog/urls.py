from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index-blog'),
    path('curtir_post/<int:id_post>/',views.curtir_post,name='curtir_post'),
    path('excluir_curtida/<int:id_curtida>/',views.excluir_curtida,name='excluir_curtida'),
    path('pegar_comentario/<int:id_post>/', views.pegar_comentario, name='pegar_comentario'),
    path('criar_post/',views.criar_post,name = 'criar_post'),
    path('filtrar_post_autor/',views.filtrar_post_autor,name='filtrar_post_autor'),
    path('filtrar_post_curtidos/',views.filtrar_post_curtidos,name='filtrar_post_curtidos')

]