from django.shortcuts import render

from .models import Post,ComentarioPost,CurtidaPost

from django.http import JsonResponse
from django.db import IntegrityError

def index (request):
    
    posts = Post.objects.all()
    try:
        curtida = CurtidaPost.objects.filter(autor=request.user).values_list('id_post', flat=True)
    except:
        curtida = []
        
    context = {
        'posts': posts,
        'curtida':curtida
    }
    
    return render(request,'index.html',context)



def criar_post(request,form):
    
    user = request.user
    titulo = form['titulo']
    descricao = form['descricao']
    
    try:
        
        post = Post(autor = user,titulo = titulo,descricao = descricao)
        post.save()
        return True
    
    except:
        
        return False
    
def comentar_post (request,context):
    
    id_post = context['id_post']
    descricao = context['descricao']
    autor = request.user
    
    try:
        
        comentario = ComentarioPost(autor = autor, id_post = id_post, descricao = descricao )
        comentario.save()
        return True
    
    except:
        
        return False
    
def excluir_comentario (request,id_comentario):
    
    user = request.user
    
    try:
        
        comentario = ComentarioPost.objects.get(id = id_comentario)
        comentario.delete()
        return True
    
    except:
        
        return False  

def get_comments_view(request, id_post):
    # Obtenha os comentários do post
    comments = ComentarioPost.objects.filter(id_post=id_post).values('descricao')

    # Converta os resultados em uma lista de dicionários
    comments_list = list(comments)

    # Retorne os comentários em formato JSON
    return JsonResponse(comments_list, safe=False)










    
def curtir_post (request,id_post):
    
    autor = request.user
    post = Post.objects.get(id = id_post)

    try:
        curtida,created = CurtidaPost.objects.get_or_create(id_post=post, autor=autor)
        if created:
            return JsonResponse({'curtida': True, 'curtidas_count': CurtidaPost.objects.filter(id_post=id_post).count()})
        else:
            excluir_curtida (request,curtida.id)
            return JsonResponse({'curtida': False, 'curtidas_count': CurtidaPost.objects.filter(id_post=id_post).count()})
    except IntegrityError:
        return JsonResponse({'curtida': False, 'curtidas_count': 0})
    
def excluir_curtida (request,id_curtida):
    
    user = request.user

    try:
        curtida = CurtidaPost.objects.get(id=id_curtida)
        post_id = curtida.id_post.id  # Salvamos o ID do post antes de excluir
        curtida.delete()
        return JsonResponse({'curtida': True, 'curtidas_count': CurtidaPost.objects.filter(id_post=post_id).count()})
    except:
        return JsonResponse({'curtida': False, 'curtidas_count': 0})
    
    