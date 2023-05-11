from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate
import usuario.views
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/auth/login")
def home(request):
    string = "Variavel"
    return render(request, 'index.html', {'string': string})


def home_tipoproduto(request):
    #view = TipoProduto.objects.all
    data = {}
    data['db'] = TipoProduto.objects.all()
    return render(request, 'home_tipoproduto.html', data)

def insert_tipoproduto(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')

        tipoproduto = TipoProduto(descricao=descricao)

        tipoproduto.save()
        #retorna para o home
        return home_tipoproduto(request)

    elif request.method == "GET": 
        return render(request, 'insert_tipoproduto.html')

def home_produto(request):
    #view = TipoProduto.objects.all
    data = {}
    data['db'] = Produto.objects.all()
    return render(request, 'home_produto.html', data)

def insertproduto(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        print("Descricao:" + descricao)
        valor = request.POST.get('valor')
        print("Valor:" + valor)
        idtipoproduto = request.POST.get('tipoproduto')
        print("ID Tipo produto:" + idtipoproduto)
        id = TipoProduto.objects.get(id=idtipoproduto)
        print("ID:")
        print(id)
        produto = Produto(descricao=descricao, valor=valor, fktipoproduto=id)

        produto.save()

        return home_produto(request)


    elif request.method == "GET":
        data = {}
        data['db'] = TipoProduto.objects.all()
        return render(request, 'insert_produto.html', data)

def editarproduto(request, id):

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        print("Descricao:" + descricao)

        valor = request.POST.get('valor')
        print("Valor:" + valor)

        tipoproduto = request.POST.get('tipoproduto')
        print("Tipo produto:" + tipoproduto)
        
        pegatipoproduto = TipoProduto.objects.get(id=tipoproduto)
        print(pegatipoproduto)
        #print(id.query)

        produto = Produto(id=id, descricao=descricao, valor=valor, fktipoproduto=pegatipoproduto)

        produto.save()

        return home_produto(request)
    elif request.method == "GET":

        data = {}
        data['produto'] = Produto.objects.get(id=id)
        data['tipoproduto'] = TipoProduto.objects.all()

        print(data)

        return render(request, 'update_produto.html', data)

def apagarproduto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return home_produto(request)