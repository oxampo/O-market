from django.contrib import admin

# Register your models here.


#Django
from django.contrib import admin

#Models

from modelsUTILS.models import *
@admin.register(Puzzle)
class PuzzleAdmin(admin.ModelAdmin):

    pass

@admin.register(Orden)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    pass