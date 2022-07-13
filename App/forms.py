from django import forms

class Usuario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    correo=forms.EmailField()
    telefono=forms.IntegerField()
    direccion=forms.CharField()
    sexo=forms.CharField()

class Productos(forms.Form):
    nombre=forms.CharField(max_length=50)
    marca=forms.CharField(max_length=50)
    fragancia=forms.CharField(max_length=30)
    sexo=forms.CharField(max_length=6)
    tamaño=forms.CharField(max_length=10)
    precio=forms.IntegerField()
    
class Descuento(forms.Form):
    descuento=forms.CharField(max_length=10)
    precio_final=forms.CharField(max_length=10)