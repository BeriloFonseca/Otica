from django.db import models

# Create your models here.

class Product(models):
    name = models.CharField('name', max_length=100)
    price = models.DateField('price', decimal_places=2, max_digits=7)
