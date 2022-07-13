
from django.db import models



class Crear_usuario(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    correo=models.EmailField(max_length=50)
    telefono=models.IntegerField()
    direccion=models.CharField(max_length=50)
    sexo=models.CharField(max_length=6)

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    fragancia=models.CharField(max_length=30)
    sexo=models.CharField(max_length=6)
    tamaño=models.CharField(max_length=10)
    precio=models.IntegerField()


class Promocion(models.Model):
    descuento=models.CharField(max_length=10)
    precio_final=models.CharField(max_length=10)
    

