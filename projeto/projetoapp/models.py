from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 50)
    Datavenda = models.DateField()

class Roupa(models.Model):
    id_roupa = models.AutoField(primary_key = True)
    Tamanho = models.CharField(max_length = 15, default='P')
    Preco = models.FloatField()
    Cor = models.CharField(max_length = 15, default='qualquer')