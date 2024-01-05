from django.db import models
from django.core.validators import MinValueValidator

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length = 50)
    DataVenda = models.DateField(null=True)
    LinkTel = models.CharField(max_length = 30)
    roupa_comprada = models.ManyToManyField('Roupa', blank = True)

    def __str__(self):
        roupas_compradas = ", ".join([str(roupa) for roupa in self.roupa_comprada.all()])
        return self.Nome

class Roupa(models.Model):
    idroupa = models.AutoField(primary_key = True)
    Tamanho = models.CharField(max_length=4)
    Preco = models.DecimalField(max_digits =10, decimal_places=2, null=True, validators=[MinValueValidator(0)])
    Categoria = models.CharField(max_length = 20, null = True)
    Cor = models.CharField(max_length = 15, null=True)

    
    def __str__(self):
        return f"Categoria: {self.Categoria}, ID: {self.idroupa}, Cor: {self.Cor}, Tamanho: {self.Tamanho}, Preco: {self.Preco}"