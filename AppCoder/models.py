from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    numero=models.IntegerField()
    
class Auto(models.Model):
    modelo=models.CharField(max_length=20)
    marca=models.CharField(max_length=20)
    anio=models.IntegerField()
    
class Reserva(models.Model):
    ubicacion_retiro=models.CharField(max_length=20)
    ubicacion_retorno=models.CharField(max_length=20)