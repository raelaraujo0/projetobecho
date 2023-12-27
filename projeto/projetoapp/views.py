from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import ClienteForm, RoupaForm
from .models import Cliente, Roupa

def home(request):
    return render(request, 'brecho/home.html')

def opcoescli(request):
    return render(request, 'brecho/cliente/opcoescliente.html')

def opcoesrou(request):
    return render(request, 'brecho/roupa/opcoesroupa.html')

## DIVISAO ENTRE HOME E MODULOS

def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('criar_cliente')
    else:
        form = ClienteForm()

    return render(request, 'brecho/cliente/cliente.html', {'form': form})
    
def excluir_cliente(request):
    if request.method == 'POST':
        idcliente = request.POST.get('idcliente')
        cliente = get_object_or_404(Cliente, pk=idcliente)
        cliente.delete()
        return HttpResponse({'message': 'Cliente excluído'})
    
    return render(request, 'brecho/cliente/excluircliente.html')

## DIVISAO ENTRE CLIENTES E ROUPAS

def criar_roupa(request):
    if request.method == 'POST':
        form = RoupaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('criar_roupa')
    else:
        form = RoupaForm()

    return render(request, 'brecho/roupa/roupa.html', {'form': form})

def excluir_roupa(request):
    if request.method == 'POST':
        idroupa = request.POST.get('idroupa')
        roupa = get_object_or_404(Roupa, pk=idroupa)
        roupa.delete()
        return HttpResponse({'message': 'Roupa excluida'})
    
    return render(request, 'brecho/roupa/excluirroupa.html')

######################

def listartudo(request):
    clientes = Cliente.objects.all()
    roupas = Roupa.objects.all()
    
    return render(request, 'brecho/listagem.html', {'clientes': clientes, 'roupas': roupas})
