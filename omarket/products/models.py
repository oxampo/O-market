""" Product models """
#Django
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Cuts(models.Model):
    cutName = models.CharField(max_length=30)

    def __str__(self):
        return self.cutName


class Animals(models.Model):
    animalName = models.CharField(max_length=30)

    def __str__(self):
        return self.animalName

class Pieces(models.Model):
    pieceName = models.CharField(max_length=30)
    cut_piece = models.ManyToManyField(Cuts)
    animal_piece = models.ManyToManyField(Animals)

    def __str__(self):
        return self.pieceName

class Products(models.Model):
    prodName = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    exempt = models.BooleanField(default=False)
    date = models.DateField(default=datetime.now())
    description = models.CharField(max_length=100, blank=True, null=True)
    animal_product = models.ForeignKey(Animals, on_delete=models.CASCADE)
    animal_piece = models.ForeignKey(Pieces, on_delete=models.CASCADE)

    def __str__(self):
        return self.prodName

class Price(models.Model):
    price = models.IntegerField()
    date_price = models.DateField(default=datetime.now())
    price_product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.price