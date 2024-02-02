from django.db import models
from django.core.validators import MinValueValidator

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    PrimeiroNome = models.CharField(max_length = 15, blank=True)
    SegundoNome = models.CharField(max_length = 15, blank=True)
    Link = models.CharField(max_length = 100, null=True)
    Tel = models.CharField(max_length = 12, null=True)

class Roupa(models.Model):
    idroupa = models.AutoField(primary_key = True)
    nomebrecho = models.CharField(max_length = 20, null=True)  
    Tamanho = models.CharField(max_length=4)
    Preco = models.DecimalField(max_digits =10, decimal_places=2, null=True, validators=[MinValueValidator(0)])
    Categoria = models.CharField(max_length = 20, null = True)
    Cor = models.CharField(max_length = 15, null=True)
    FotoRoupa = models.ImageField(upload_to='fotosroupas/',blank=True, null=True)

class Venda(models.Model):
    idvenda = models.AutoField(primary_key= True)
    roupa_comprada = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    cliente_comprou = models.ForeignKey(Roupa, on_delete=models.SET_NULL, null=True)
    DataVenda = models.DateField(null=True)

    def __str__(self):
        clientes_comprou = ", ".join([str(cliente) for cliente in self.cliente_comprou.all()])
        roupas_compradas = ", ".join([str(roupa) for roupa in self.roupa_comprada.all()])