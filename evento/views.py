from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from .tasks import enviar_email
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime


from .models import Tarefa



@login_required(login_url="logar")
def painel(request):
    
    # Últimas tarefas cadastradas
    ultimas_tarefas = Tarefa.objects.filter(user=request.user).order_by('-id')[:3]
    
    # Tarefas prestes a vencer
    tarefas_perto_de_vencer = Tarefa.objects.filter(user=request.user, prazo__gt=timezone.now(),status = 'P').order_by('prazo')[:3]

    context = {
        'ultimas_tarefas': ultimas_tarefas,
        'tarefas_perto_de_vencer': tarefas_perto_de_vencer,
    }
    return render(request, 'painel.html', context)




##############################################################################
####### FILTROS                                                              #  
##############################################################################

# Responsavel por renderizar cards de todas tarefas que ainda estão no prazo
@login_required(login_url="logar")
def tarefas_no_prazo(request):
    if request.method == 'GET':
        # Filtrar tarefas do usuário onde o prazo ainda não passou
        tarefas = Tarefa.objects.filter(user=request.user, prazo__gt=timezone.now(),status = "P")

        context = {
            'tarefas':tarefas
        }
        return render(request,'tarefas_filtro.html',context)
    
    
  
     
# Responsavel por renderizar cards de todas tarefas que ainda estão fora do prazo
@login_required(login_url="logar")
def tarefas_fora_prazo(request):
    # Filtrar tarefas do usuário onde o prazo já passou
    tarefas = Tarefa.objects.filter(user=request.user, prazo__lt=timezone.now(),status = "P")

    context = {
        'tarefas':tarefas
    }
    return render(request,'tarefas_filtro.html',context)

def tarefas_total (request):
    # Filtrar tarefas do usuário onde o prazo já passou
    tarefas = Tarefa.objects.filter(user=request.user)

    context = {
        'tarefas':tarefas
    }
    return render(request,'tarefas_filtro.html',context)

@login_required(login_url="logar")
def tarefas_concluidos(request):
    # Filtrar tarefas do usuário onde já foi concluida
    tarefas = Tarefa.objects.filter(user=request.user,status = "C")

    context = {
        'tarefas':tarefas
    }
    return render(request,'tarefas_filtro.html',context)
   
   
@login_required(login_url="logar")
def tarefas_pendentes(request):
    # Filtrar tarefas do usuário onde ainda está pendente
    tarefas = Tarefa.objects.filter(user=request.user,status = "P")

    context = {
        'tarefas':tarefas
    }
    return render(request,'tarefas_filtro.html',context)    







##############################################################################
####### CRUD                                                                 #  
##############################################################################

# Responsavel por renderizar form de criação de uma tarefa
@login_required(login_url="logar")
def criar_tarefa(request):
    if request.method == 'GET':
        return render(request, "criar_tarefa.html")
    else:    
        context = {
            'titulo': request.POST.get('titulo'),
            'descricao': request.POST.get('descricao'),
            'datetime': request.POST.get('datetime'),
            'email':request.POST.get('email')
        }

        if not salvar_tarefa(request,context):
            return HttpResponse('Erro ao salvar uma nova tarefa')
        return render(request, "criar_tarefa.html")

# Responsavel por renderizar form de edição de uma tarefa recebendo na url o parametro id da mesma
@login_required(login_url="logar")
def editar_tarefa(request,tarefa_id):
    
    tarefa = get_object_or_404(Tarefa,user = request.user,id = tarefa_id)
    if request.method == 'GET':
        return render(request, "editar_tarefa.html",{'tarefa':tarefa})
    else:    
        context = {
            'titulo': request.POST.get('titulo'),
            'descricao': request.POST.get('descricao'),
            'datetime': request.POST.get('datetime'),
            'email':request.POST.get('email')
        }

        if not salvar_editar_tarefa(context,tarefa):
            return HttpResponse('Erro ao salvar uma nova tarefa')
        return redirect('/evento/painel/')
    
# Responsavel por excluir uma tarefa recebendo na url o parametro id da mesma
def excluir_tarefa(request,tarefa_id):
    tarefa = get_object_or_404(Tarefa, user = request.user, id = tarefa_id )
    tarefa.delete()
    return redirect('/evento/painel/')

# Responsavel por editar o status de uma tarefa recebendo na url o parametro id da mesma e o novo status
def editar_status_tarefa (request,status,tarefa_id):
        editarStatus = Tarefa.objects.get(id=tarefa_id,user = request.user)
        editarStatus.status = status
        editarStatus.save()
        return redirect("/evento/painel/")     




# Salva no banco de dados edições de uma tarefa especifica
def salvar_editar_tarefa(dir,tarefa):
    try:
        # Converte a string de data e hora para um objeto datetime
        datetime_obj = datetime.strptime(dir['datetime'], "%Y-%m-%dT%H:%M")

        # Cria um objeto datetime consciente associando-o com o fuso horário padrão
        aware_datetime = timezone.make_aware(datetime_obj)

        tarefa.titulo=dir['titulo']
        tarefa.email=dir['email']
        tarefa.descricao=dir['descricao']
        tarefa.prazo=aware_datetime
        tarefa.save()
        return True
    except Exception as e:
        print(e)
        return False

# Salva no banco de dados uma nova tarefa
def salvar_tarefa(request,dir):
    try:
        # Converte a string de data e hora para um objeto datetime
        datetime_obj = datetime.strptime(dir['datetime'], "%Y-%m-%dT%H:%M")

        # Cria um objeto datetime consciente associando-o com o fuso horário padrão
        aware_datetime = timezone.make_aware(datetime_obj)

        tarefa = Tarefa(user=request.user,titulo=dir['titulo'],email=dir['email'], descricao=dir['descricao'], prazo=aware_datetime)
        tarefa.save()
        return True
    except Exception as e:
        print(e)
        return False
