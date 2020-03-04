""" Product models """
#Django
from django.contrib.auth.models import User
from django.db import models


class Corts(models.Model):
    corte = models.CharField(max_length=30)

    def __str__(self):
        return self.corte


class Animals(models.Model):
    animal = models.CharField(max_length=30)

    def __str__(self):
        return self.animal


class Products(models.Model):
    prodName = models.CharField(max_length=30)
    precio = models.IntegerField()
    disponibles = models.IntegerField(default=0)
    animal = models.ForeignKey(Animals, on_delete=models.CASCADE)
    corte = models.ForeignKey(Corts, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
