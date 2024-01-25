from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import ClienteForm, RoupaForm, VendaForm
from .models import Cliente, Roupa, Venda

def home(request):
    roupas = Roupa.objects.all()
    return render(request, 'brecho/home.html', {'roupas': roupas })

def opcoescli(request):
    return render(request, 'brecho/cliente/opcoescliente.html')

def opcoesrou(request):
    return render(request, 'brecho/roupa/opcoesroupa.html')

def opcoesven(request):
    return render(request, 'brecho/venda/opcoesvendas.html')


def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente criado com sucesso')
            return redirect('criar_cliente')
    else:
        form = ClienteForm()

    return render(request, 'brecho/cliente/cliente.html', {'form': form})
    
def excluir_cliente(request, idcliente):
    if request.method == 'POST':
        idcliente = request.POST.get('idcliente')
        cliente = get_object_or_404(Cliente, pk=idcliente)
        cliente.delete()
        messages.success(request, 'Cliente deletado')
        return redirect('excluir_cliente')
    
    return render(request, 'brecho/cliente/excluircliente.html')

def atualizar_cliente(request, idcliente):
    form = None
    cliente = None

    if request.method == 'POST':
        idcliente = request.POST.get('idcliente')
        cliente = get_object_or_404(Cliente, pk=idcliente)
        form = ClienteForm(request.POST or None, instance=cliente)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso')
            return redirect('atualizar_cliente')

    return render(request, 'brecho/cliente/atualizarcliente.html', {'form': form, 'cliente': cliente })  

def criar_roupa(request):
    if request.method == 'POST':
        form = RoupaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Roupa criada com sucesso')
            return redirect('criar_roupa')
    else:
        form = RoupaForm()

    return render(request, 'brecho/roupa/roupa.html', {'form': form})

def excluir_roupa(request, idroupa):
    if request.method == 'POST':
        idroupa = request.POST.get('idroupa')
        roupa = get_object_or_404(Roupa, pk=idroupa)
        roupa.delete()
        messages.success(request, 'Roupa deletada')
        return redirect('excluir_roupa')
    
    return render(request, 'brecho/roupa/excluirroupa.html')

def atualizar_roupa(request, idroupa):
    form = None
    roupa = None

    if request.method == 'POST':
        idroupa = request.POST.get('idroupa')
        roupa = get_object_or_404(Roupa, pk=idroupa)
        form = RoupaForm(request.POST or None, instance=roupa)

        if form.is_valid():
            form.save()
            messages.success(request, 'Roupa atualizada com sucesso')
            return redirect('atualizar_roupa')

    return render(request, 'brecho/roupa/atualizarroupa.html', {'form': form, 'roupa': roupa})

def criar_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venda registrada')
            return redirect('criar_venda')
    else:
        form =VendaForm()

    return render(request, 'brecho/venda/venda.html', {'form': form})

def excluir_venda(request, idvenda):
    if request.method == 'POST':
        idvenda = request.POST.get('idvenda')
        venda = get_object_or_404(Venda, pk=idvenda)
        venda.delete()
        messages.success(request, 'Venda deletada')
        return redirect('excluir_venda')
    
    return render(request, 'brecho/venda/excluirvenda.html')

def atualizar_venda(request, idvenda):
    form = None
    venda = None
    
    if request.method == 'POST':
        idvenda = request.POST.get('idvenda')
        venda = get_object_or_404(Venda, pk=idvenda)
        form = VendaForm(request.POST or None, instance=venda)

        if form.is_valid():
            form.save()
            messages.success(request, 'Venda atualizada com sucesso')

    return render(request, 'brecho/venda/atualizarvenda.html', {'form': form, 'venda': venda})