from django.db import models
from autenticacao.models import Users

class Tarefa (models.Model):
    STATUS_CHOICE = [
        ("P","Pendente"),
        ("C","Concluido")
    ]
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    prazo = models.DateTimeField()
    email = models.EmailField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default= "P")
    data_mensagem = models.DateField(null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="user")
    