from django.db import models

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length = 50)
    DataVenda = models.DateField(null=True)
    LinkTel = models.CharField(max_length = 30)
    roupa_comprada = models.ManyToManyField('Roupa', blank = True)

    def __str__(self):
        return self.clientes

class Tamanho(models.Model):
    nome = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.nome

class Roupa(models.Model):
    idroupa = models.AutoField(primary_key = True)
    tamanhos = models.ManyToManyField(Tamanho)
    Preco = models.FloatField(null=True)
    Categoria = models.CharField(max_length = 20, null = True)
    Cor = models.CharField(max_length = 15, null=True)

    
    def __str__(self):
        return self.roupas