from django.db import models

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length = 50)
    DataVenda = models.DateField(null=True)

    def __str__(self):
        return self.clientes

class Roupa(models.Model):
    idroupa = models.AutoField(primary_key = True)
    Tamanho = models.CharField(max_length = 15, null=True)
    Preco = models.FloatField(null=True)
    Cor = models.CharField(max_length = 15, null=True)
    
    def __str__(self):
        return self.roupas