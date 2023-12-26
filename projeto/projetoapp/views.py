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
    
def excluir_cliente(request):
    if request.method == 'POST':
        idcliente = request.POST.get('idcliente')
        cliente = get_object_or_404(Cliente, pk=idcliente)
        cliente.delete()
        return JsonResponse({'message': 'Cliente excluído'})
    
    return redirect('excluir_cliente')


def criar_roupa(request):
    if request.method == 'POST':
        form = RoupaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RoupaForm()

    return render(request, 'brecho/roupa/roupa.html', {'form': form})

def excluir_roupa(request):
    if request.method == 'POST':
        idroupa = request.POST.get('idroupa')
        roupa = get_object_or_404(Roupa, pk=idroupa)
        roupa.delete()
        return JsonResponse({'message': 'Roupa excluida'})
    
    return redirect('excluir_roupa')

def listartudo(request):
    clientes = Cliente.objects.all()
    roupas = Roupa.objects.all()
    
    return render(request, 'brecho/listagem.html', {'clientes': clientes, 'roupas': roupas})