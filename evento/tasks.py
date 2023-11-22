from celery import shared_task
from .models import Tarefa
from django.core.mail import send_mail

from django.utils import timezone



@shared_task
def verificar_prazo():
    tarefas = Tarefa.objects.all()


    for tarefa in tarefas:
        prazo = tarefa.prazo
        agora = timezone.now()
        status = tarefa.status
        email = tarefa.email
        titulo = tarefa.titulo
        data_mensagem = tarefa.data_mensagem

        if prazo < agora and status == "P" and not data_mensagem:
            print(f'O prazo da tarefa {tarefa.id} já venceu. Enviar e-mail de lembrete.')
            enviar_email(email,titulo)
            data = tarefa
            data.data_mensagem = agora
            data.save()
        else:
            print(f'O prazo da tarefa {tarefa.id} ainda não venceu.')
            
            
def enviar_email(email,titulo):
    subject = f'Lembrete: Prazo da Tarefa {titulo} Vencido'
    message = 'O prazo da sua tarefa venceu. Por favor, tome as providências necessárias.'
    from_email = 'seu_email@gmail.com'  # Substitua pelo seu endereço de e-mail
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
            