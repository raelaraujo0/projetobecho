from django import forms
from .models import Cliente, Roupa, Tamanho

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['Nome', 'DataVenda', 'LinkTel', 'roupa_comprada']

class RoupaForm(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ['tamanhos', 'Preco', 'Cor', 'Categoria']

    tamanhos = forms.ModelMultipleChoiceField(
        queryset=Tamanho.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )