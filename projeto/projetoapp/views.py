from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .forms import ClienteForm, RoupaForm
from .models import Cliente, Roupa

def home(request):
    return render(request, 'brecho/home.html')

def opcoescli(request):
    return render(request, 'brecho/cliente/baseC.html')

def opcoesrou(request):
    return render(request, 'brecho/roupa/baseR.html')


def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClienteForm()

    return render(request, 'brecho/cliente/cliente.html', {'form': form})
    
def excluir_cliente(request, idcliente):
    cliente = get_object_or_404(Cliente, pk=idcliente)
    
    if request.method == 'POST':
        cliente.delete()
        return JsonResponse({'message': 'Cliente excluído'})
    
    return render(request, 'brecho/cliente/excluircliente.html', {'cliente': cliente})


def criar_roupa(request):
    if request.method == 'POST':
        form = RoupaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RoupaForm()

    return render(request, 'brecho/roupa/roupa.html', {'form': form})

def excluir_roupa(request, idroupa):
    roupa = get_object_or_404(Roupa, pk=idroupa)
    
    if request.method == 'POST':
        roupa.delete()
        return JsonResponse({'message': 'Roupa deletada'})
    
    return render(request, 'brecho/roupa/excluirroupa.html', {'roupa': roupa})

def listartudo(request):
    clientes = Cliente.objects.all()
    roupas = Roupa.objects.all()
    
    return render(request, 'brecho/listagem.html', {'clientes': clientes, 'roupas': roupas})