from django.shortcuts import render,redirect

from .models import Post,ComentarioPost,CurtidaPost

from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from django.contrib.messages import constants
from django.contrib import messages

def index (request):
    if request.method == "POST":
        context = {
            'id_post': request.POST['id_post'],
            'descricao':request.POST['descricao']
        }
        comentar_post (request,context)
    
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

@login_required(login_url="logar")
def filtrar_post_autor(request):
    posts = Post.objects.filter(autor = request.user)
    try:
        curtida = CurtidaPost.objects.filter(autor=request.user).values_list('id_post', flat=True)
    except:
        curtida = []
        
    context = {
        'posts': posts,
        'curtida':curtida
    }
    
    return render(request,'index.html',context)
@login_required(login_url="logar")
def filtrar_post_curtidos (request):
    try:
        curtidas = CurtidaPost.objects.filter(autor=request.user).values_list('id_post', flat=True)
        # Filtrar os posts com base nos IDs obtidos
        posts_curtidos = Post.objects.filter(id__in=curtidas)
             
    except:
        curtidas = []
        posts_curtidos = []
        
    context = {
        'posts': posts_curtidos,
        'curtida':curtidas
    }
    
    return render(request,'index.html',context)
    
@login_required(login_url="logar")
def criar_post(request):
    
    
    if request.method == 'GET':
        return render(request,'criar_post.html')
    else:    
        user = request.user
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        
        try:
            
            post = Post(autor = user,titulo = titulo,descricao = descricao)
            post.save()
            return redirect('/blog/')
        except:
            messages.add_message(request,constants.ERROR,"Ocorreu um erro ao criar seu post")
            return render(request,'criar_post.html')
@login_required(login_url="logar")        
def comentar_post (request,context):
    
    id_post = context['id_post']
    descricao = context['descricao']
    autor = request.user
    
    try:
        id_post = Post.objects.get(id = id_post)
        comentario = ComentarioPost(autor = autor, id_post = id_post, descricao = descricao )
        comentario.save()
        return True
    
    except Exception as e :
        print(e)
        return False  
    
def excluir_comentario (request,id_comentario):
    
    user = request.user
    
    try:
        
        comentario = ComentarioPost.objects.get(id = id_comentario)
        comentario.delete()
        return True
    
    except:
        
        return False  

def pegar_comentario(request, id_post):
    # Obtenha os comentários do post
    comments = ComentarioPost.objects.filter(id_post=id_post).values('descricao')

    # Converta os resultados em uma lista de dicionários
    comments_list = list(comments)

    # Retorne os comentários em formato JSON
    return JsonResponse(comments_list, safe=False)










@login_required(login_url="logar")
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
@login_required(login_url="logar")    
def excluir_curtida (request,id_curtida):
    
    user = request.user

    try:
        curtida = CurtidaPost.objects.get(id=id_curtida)
        post_id = curtida.id_post.id  # Salvamos o ID do post antes de excluir
        curtida.delete()
        return JsonResponse({'curtida': True, 'curtidas_count': CurtidaPost.objects.filter(id_post=post_id).count()})
    except:
        return JsonResponse({'curtida': False, 'curtidas_count': 0})
    
    