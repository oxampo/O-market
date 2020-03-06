from django.db import models

# Create your models here.
"""  Project models """
#Django

#Models
from users.models import Profile,Addresses
from products.models import Price, Products

class Puzzle(models.Model):

    enunciado = models.CharField(max_length=100,blank=False,null=True)
    activo = models.BooleanField(blank=True,null=True)
    descuento = models.PositiveSmallIntegerField(blank=False, null=True)
    dificultad = models.PositiveSmallIntegerField(blank=False,null=True) 


class Orden(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    fecha = models.DateTimeField(blank=False, null=True,auto_now_add=True)
    iva = models.PositiveSmallIntegerField(blank=False, null=True)
    instrumento_pago = models.CharField(max_length=15, blank=False,null=True)
    totalBruto = models.PositiveIntegerField(blank=False, null=True)
    totalNeto = models.PositiveIntegerField(blank=False, null=True)

class OrderDetails(models.Model):
    Price_Id = models.ForeignKey(Price,on_delete=models.CASCADE)
    cantidad_orden = models.PositiveSmallIntegerField(blank=False, null=True)

class PuzzlesPorOrdenes (models.Model):
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    acertado = models.BooleanField(blank=True, null=True)
    descuesto_total = models.PositiveSmallIntegerField(blank=False,null=True)


class Delivery(models.Model):
    orden = models.OneToOneField(Orden, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Addresses, on_delete=models.CASCADE)
    entregado = models.BooleanField(blank=False, null=True)

class PrecioActual(models.Model):
    Nombre = models.CharField(max_length=100)
    Cantidad = models.IntegerField()
    Animal = models.CharField(max_length=100)
    Pieza = models.CharField(max_length=100)
    Precio = models.CharField(max_length=100)
    Fecha = models.DateField(max_length=100) 
    class Meta:
        managed = False
        db_table = 'precio_actual'

class PuzzleAcierto(models.Model):
    Puzzle = models.CharField(max_length=100)
    Aciertos = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'puzzle_acertados' 
