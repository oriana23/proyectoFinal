from django import forms

class Usuario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    correo=forms.EmailField()
    telefono=forms.IntegerField()
    direccion=forms.CharField()
    sexo=forms.CharField()
