from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Users,Endereco,Celular

from django.contrib.messages import constants
from django.contrib import messages


import requests
from django.http import JsonResponse

# Templates
def logar (request):
    if request.user.is_authenticated :          
        return redirect ("/")
    else:
        if request.method == "GET":
            return render(request,"logar.html")
        else:
            
            email = request.POST.get("email")
            senha = request.POST.get("password")
            
            username = get_username_from_email(email)
            if not username:
                messages.add_message(request,constants.ERROR,"Email não existe")    
                return render (request, "logar.html")  
            
            # Verificando de senha existe
            usuario_autenticado= authenticate(username=username, password=senha)
            
            #Verificando se usuario e senha existe
            if usuario_autenticado:
                login(request,usuario_autenticado)   
                return redirect ("/")
            else:
                messages.add_message(request,constants.ERROR,"Senha Incorreta")
                return render (request, "logar.html")
        
def cadastrar (request):
    if request.user.is_authenticated :
        return redirect ("/")
    else:
        if request.method == "GET":
            return render(request,"cadastrar.html")
        else:
            usuario = request.POST.get("usuario")
            senha = request.POST.get("password")
            confirm_senha = request.POST.get("confirmSenha")
            email = request.POST.get("email")
                     
            usuarioExiste =  Users.objects.filter(username = usuario).exists()
            emailExiste =  Users.objects.filter(email = email).exists()

            if usuarioExiste:
                messages.add_message(request,constants.ERROR,"Nome de usuario já existe")    
                return render (request, "cadastrar.html")
            elif emailExiste:
                messages.add_message(request,constants.ERROR,"Email já existe")    
                return render (request, "cadastrar.html")  
            elif len(senha.strip()) < 8:
                messages.add_message(request,constants.ERROR,"Senha muito fraca")    
                return render (request, "cadastrar.html") 
            elif not senha == confirm_senha:
                messages.add_message(request,constants.ERROR,"As senhas não conferem")
                return render (request, "cadastrar.html")

            try:
                Users.objects.create_user(username = usuario,email=email,password=senha)
                messages.add_message(request,constants.SUCCESS,"Usuario cadastrado com sucesso")
                return redirect ("/auth/logar")
            except:
                messages.add_message(request,constants.ERROR,"Ocorreu um erro na gravação do seu cadastrar")
                return render(request,"cadastrar.html")
        

def deslogar(request):
    logout(request)
    return redirect("/")



def get_username_from_email(email):
    try:
        user = Users.objects.get(email = email)
        return user.username
    except:
        return False
    
