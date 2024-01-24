from django.db import models
from django.core.validators import MinValueValidator

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length = 50)
    LinkTel = models.CharField(max_length = 30)

    def __str__(self):
        return f"Id: {self.idcliente}, Nome:  {self.Nome}, Link/Tel: {self.LinkTel}"

class Roupa(models.Model):
    idroupa = models.AutoField(primary_key = True)
    nomebrecho = models.CharField(max_length = 20, null=True)  
    Tamanho = models.CharField(max_length=4)
    Preco = models.DecimalField(max_digits =10, decimal_places=2, null=True, validators=[MinValueValidator(0)])
    Categoria = models.CharField(max_length = 20, null = True)
    Cor = models.CharField(max_length = 15, null=True)
    FotoRoupa = models.ImageField(upload_to='fotosroupas/',blank=True, null=True)

    def __str__(self):
        return f"Categoria: {self.Categoria}, ID: {self.idroupa}, Cor: {self.Cor}, Tamanho: {self.Tamanho}, Preco: {self.Preco}"

class Venda(models.Model):
    idvenda = models.AutoField(primary_key= True)
    roupa_comprada = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    cliente_comprou = models.ForeignKey(Roupa, on_delete=models.SET_NULL, null=True)
    DataVenda = models.DateField(null=True)

    def __str__(self):
        clientes_comprou = ", ".join([str(cliente) for cliente in self.cliente_comprou.all()])
        roupas_compradas = ", ".join([str(roupa) for roupa in self.roupa_comprada.all()])
        return self.vendas