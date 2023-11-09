from django.db import models
from django.contrib.auth.models import AbstractUser





class Endereco(models.Model):
    # Lista de escolhas para os estados brasileiros
    ESTADOS_BRASILEIROS = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=ESTADOS_BRASILEIROS)
    cep = models.CharField(max_length=9)  # O CEP no Brasil tem o formato "XXXXX-XXX".

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade}, {self.estado} - CEP: {self.cep}"
    
class Celular(models.Model):
    numero = models.CharField(max_length=15)
    
class Users (AbstractUser):
    endereco = models.ManyToManyField(Endereco)
    celular = models.ManyToManyField(Celular)
