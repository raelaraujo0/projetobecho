from django.shortcuts import render
from .models import Cliente, Roupa

def home(request):
    return render(request, 'brecho/home.html')

def listar_clientes(request):
    if request.method == 'POST':
        novo_cliente = Cliente()
        novo_cliente.nome = request.POST.get('nome')
        novo_cliente.FotoCliente = request.POST.get('FotoCliente')
        novo_cliente.Datavenda = request.POST.get('DataVenda')
    
    clientes = {
        'clientes': Cliente.objects.all()
    }

    return render (request, 'brecho/cliente.html', clientes)

def listar_roupas(request):
    if request.method == 'POST':
        nova_roupa = Roupa()
        nova_roupa.Tamanho = request.POST.get('Tamanho')
        nova_roupa.FotoRoupa = request.POST.get('FotoRoupa')
        nova_roupa.Cor = request.POST.get('Cor')
        nova_roupa.Preco = request.POST.get('Preco')

    roupas = {
        'roupas': Roupa.objects.all()
    }

    return render (request, 'brecho/roupa.html', roupas)