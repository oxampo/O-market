""" Product models """
from django.db import models

# Create your models here.

class User(models.Model):
    """ User model """

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True, blank=True)

    password = models.CharField(max_length=100)

    address = models.CharField(max_length=100, blank=True)

    number_of_purchases = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)