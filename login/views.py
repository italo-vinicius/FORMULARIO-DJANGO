from django.shortcuts import render
from django.http import HttpResponse
from .models import Cadastro

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        
        pessoa = Cadastro(
            nome=nome,
            email=email,
            cpf=cpf,
            senha=senha
        )
        pessoa.save()
        return HttpResponse('Dados cadastrados com sucesso')