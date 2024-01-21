from django import forms
from .models import Cliente, Roupa, Venda

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["idcliente", "Nome", "LinkTel"]

class RoupaForm(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ["idroupa", "Tamanho", "Preco", "Cor", "Categoria", "FotoRoupa"]

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ["idvenda", "DataVenda","cliente_comprou" ,"roupa_comprada"]
