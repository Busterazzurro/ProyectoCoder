from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    numero=models.IntegerField()
    
    def __str__(self):
        return f'Cliente Numero:  {self.numero}'
    
class Auto(models.Model):
    modelo=models.CharField(max_length=20)
    marca=models.CharField(max_length=20)

    def __str__(self):
        return f'Auto Numero:  {self.numero}'
    
class Viaje(models.Model):
    ubicacion_retiro=models.CharField(max_length=20)
    ubicacion_retorno=models.CharField(max_length=20)
    conductor=models.CharField(max_length=20)
    preferencia_aire_acondicionado=models.BooleanField()
    preferencia_musica=models.BooleanField()
    forma_de_pago=models.CharField(max_length=10)
    numero=models.IntegerField()
    
    def __str__(self):
        return f'Viaje Numero:  {self.numero}'
    