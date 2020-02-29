""" Product models """
#Django
from django.contrib.auth.models import User
from django.db import models

class Products(models.Model):
    prodName = models.CharField(max_length=30)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=100, blank=True, null=True)
