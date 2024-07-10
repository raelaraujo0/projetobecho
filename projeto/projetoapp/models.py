from django.db import models
from django.core.validators import MinValueValidator

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nomeCliente = models.CharField(max_length= 100, null=True)
    Link = models.CharField(max_length = 100, null=True)
    Tel = models.CharField(max_length = 12, null=True)

class Roupa(models.Model):
    idRoupa = models.AutoField(primary_key = True)
    nomeBrecho = models.CharField(max_length = 20, null=True)  
    Tamanho = models.CharField(max_length=4)
    Preco = models.DecimalField(max_digits =10, decimal_places=2, null=True, validators=[MinValueValidator(0)])
    Categoria = models.CharField(max_length = 20, null = True)
    Cor = models.CharField(max_length = 15, null=True)
    FotoRoupa = models.ImageField(upload_to='fotosroupas/',blank=True, null=True)

class Venda(models.Model):
    idVenda = models.AutoField(primary_key= True)
    roupaComprada = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    clienteComprou = models.ForeignKey(Roupa, on_delete=models.SET_NULL, null=True)
    dataVenda = models.DateField(null=True)

    def __str__(self):
        clientes_comprou = ", ".join([str(cliente) for cliente in self.clienteComprou.all()])
        roupas_compradas = ", ".join([str(roupa) for roupa in self.roupaComprada.all()])