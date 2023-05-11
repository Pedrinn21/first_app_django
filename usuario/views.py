from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_session
import produto.views

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')

    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe usuário com esse username')

        else:
            
            ###CRIA USUARIO
            user = User.objects.create_user(username=username, email=email, password=senha)
            user.save()

            return render(request, 'login.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    else:
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(username=username, password=senha)

        if user:
            login_session(request, user)
            return produto.views.home(request)
        
        else:
            return HttpResponse('Usuario ou senha inválidos!')