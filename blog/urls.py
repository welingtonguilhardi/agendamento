from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index-blog'),
    path('curtir_post/<int:id_post>/',views.curtir_post),
    path('excluir_curtida/<int:id_curtida>/',views.excluir_curtida),
    path('get_comments/<int:id_post>/', views.get_comments_view, name='get_comments'),
]