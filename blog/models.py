from django.db import models
from autenticacao.models import Users
from django.utils import timezone
class Post (models.Model):
    
    autor = models.ForeignKey(Users,on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now())
    
    def usuario_curtiu(self, user):
        return self.curtidapost_set.filter(autor=user).exists()
    
class CurtidaPost (models.Model):
    
    autor = models.ForeignKey(Users,on_delete=models.DO_NOTHING)
    id_post = models.ForeignKey(Post,on_delete=models.DO_NOTHING)
    
    class Meta:
        # Garante que um usuário só possa curtir um post uma vez
        constraints = [
            models.UniqueConstraint(fields=['autor', 'id_post'], name='unique_curtida')
        ]
    
class ComentarioPost (models.Model):
    
    autor = models.ForeignKey(Users,on_delete=models.DO_NOTHING)
    id_post = models.ForeignKey(Post,on_delete=models.DO_NOTHING)
    descricao = models.TextField()
    
    
    
