from django import http
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from App.models import *
from App.forms import *


def usuario(request):
    if request.method =='POST':

        formulario= Usuario(request.POST)
        print(formulario)
        
        if formulario.is_valid:

            informacion= formulario.cleaned_data
            usuario= Crear_usuario(nombre= informacion['nombre'], apellido= informacion['apellido'], correo= informacion['correo'], telefono= informacion['telefono'], direccion= informacion['direccion'], sexo= informacion['sexo'],)

            usuario.save()

            return render(request, "App/inicio.html")

    else:
        formulario= Usuario()
    return render(request, "App/usuario.html", {"formulario":formulario})



    

def producto(request):
    return render(request, "App/producto.html")

def inicio(request):
    return render(request, "App/inicio.html")


