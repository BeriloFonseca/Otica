from django.db import models

class Product(models.Model):
    name = models.CharField('name', max_length=100)
    price = models.DecimalField('price', decimal_places=2, max_digits=7)
    amount = models.IntegerField('amount')
    def __str__(self):
        return self.nome

class Client(models.Model):
    name = models.CharField('name', max_length=100)
    surname = models.DecimalField('surname', decimal_places=2, max_digits=100)
    email = models.IntegerField('email',max_length=100)

class Compras(models.Model):
    Produto = models.CharField('name', max_length=100)
    Parcelas = models.DecimalField('surname', decimal_places=2, max_digits=100)
    Contato = models.IntegerField('email',max_length=100)