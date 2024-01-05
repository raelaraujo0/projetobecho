from django import forms
from .models import Cliente, Roupa

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['Nome', 'DataVenda', 'LinkTel']

class RoupaForm(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ['Tamanho', 'Preco', 'Cor']