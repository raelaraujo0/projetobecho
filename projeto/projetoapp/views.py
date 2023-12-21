from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Cliente, Roupa

def home(request):
    return render(request, 'brecho/home.html')

def criar_cliente(request):
    if request.method == 'POST':
        novo_cliente = Cliente()
        novo_cliente.nome = request.POST.get('nome')
        novo_cliente.FotoCliente = request.POST.get('FotoCliente')
        novo_cliente.Datavenda = request.POST.get('DataVenda')
        novo_cliente.save()
        return HttpResponse('Cliente Criado')
    
def criar_roupa(request):
    if request.method == 'POST':
        nova_roupa = Roupa()
        nova_roupa.Tamanho = request.POST.get('Tamanho')
        nova_roupa.FotoRoupa = request.POST.get('FotoRoupa')
        nova_roupa.Cor = request.POST.get('Cor')
        nova_roupa.Preco = request.POST.get('Preco')
        nova_roupa.save()
        return HttpResponse('Roupa Criada')
_
def excluir_cliente(_, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    cliente.delete()
    return JsonResponse({'message: Cliente excluido'})

def excluir_roupa(_, id_roupa):
    roupa = get_object_or_404(Roupa, pk=id_roupa)
    roupa.delete()
    return JsonResponse({'message: Roupa deletada'})

def listartudo(request):
    clientes = Cliente.objects.all()
    roupas = Roupa.objects.all()
    
    return render(request, 'brecho/listagem.html', {'clientes': clientes, 'roupas': roupas})