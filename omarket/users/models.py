
""" Users models """

#Django
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    """ Profile model
    
    Proxy model that extends the base data with other
    information
    
     """
    #OneToOne es para relaciones al borrarse 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user ya recibe lo de los nombres, username, etc
    address = models.CharField(max_length=100, blank=True, null=True)
    nro_purchases = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.user.username
