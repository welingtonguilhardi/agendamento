
from django.urls import path
from . import views


urlpatterns = [
    # Filtro
    path("no_prazo/",views.tarefas_no_prazo,name='tarefas_no_prazo'),
    path("tarefas_total/",views.tarefas_total,name='tarefas_total'),
    path("fora_prazo/",views.tarefas_fora_prazo,name='tarefas_fora_prazo'),
    path("concluidos/",views.tarefas_concluidos,name='tarefas_concluidos'),
    path("pendentes/",views.tarefas_pendentes,name='tarefas_pendentes'),
    # CRUD
    path("criar/",views.criar_tarefa,name='criar_tarefa'),
    path("editar/<int:tarefa_id>/",views.editar_tarefa,name='editar_tarefa'),
    path("editar_status/<str:status>/<int:tarefa_id>/",views.editar_status_tarefa,name='editar_status_tarefa'),
    path("excluir/<int:tarefa_id>/",views.excluir_tarefa,name='excluir_tarefa'),
    # Painel
    path("painel/", views.painel, name='painel'),
]
