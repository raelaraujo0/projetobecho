from django.shortcuts import render
from .models import cliente, roupa

def home(request):
    return render(request, 'cliente/home.html')

def roupas(request):
    nova_roupa = roupa()
    request.POST.get('nome')
    request.POST.get('FotoCliente')
    request.POST.get('DataVenda')

def clientes(request):
    novo_cliente = cliente()
    request.POST.get('Tamanho')
    request.POST.get('FotoRoupa')
    request.POST.get('cor')
    request.POST.get('Preco')
