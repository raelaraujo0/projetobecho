from django.db import models

class cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 50)
    FotoCliente = models.ImageField()
    Datavenda = models.DateField()

class roupa(models.Model):
    id_roupa = models.AutoField(primary_key = True)
    FotoRoupa = models.ImageField()
    Preco = models.FloatField()
    Cor = models.CharField(max_length = 15)