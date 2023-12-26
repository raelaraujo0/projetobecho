from django.db import models

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 50)
    Datavenda = models.DateField()

    def __str__(self):
        return self.nome

class Roupa(models.Model):
    idroupa = models.AutoField(primary_key = True)
    Tamanho = models.CharField(max_length = 15, default='P')
    Preco = models.FloatField()
    Cor = models.CharField(max_length = 15, default='qualquer')
    
    def __str__(self):
        return self.roupa