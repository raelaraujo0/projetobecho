from django import forms
from .models import Cliente, Roupa, Venda

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["idCliente",
                "nomeCliente",
                "Link",
                "Tel"]

class RoupaForm(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ["nomeBrecho",
                "idRoupa",
                "Tamanho",
                "Categoria",
                "FotoRoupa",
                "Preco",
                "Cor"]

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ["idVenda",
                  "dataVenda",
                  "clienteComprou",
                  "roupaComprada"]
