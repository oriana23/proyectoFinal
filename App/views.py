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
    if request.method =='POST':

        formularioProducto= Productos(request.POST)
        print(formularioProducto)
        
        if formularioProducto.is_valid:

            informacion= formularioProducto.cleaned_data
            producto= Producto(nombre= informacion['nombre'], marca= informacion['marca'], fragancia= informacion['fragancia'], sexo= informacion['sexo'], tamaño= informacion['tamaño'], precio= informacion['precio'], )
            producto.save()

            return render(request, "App/inicio.html")

    else:
        formularioProducto= Productos()
    return render(request, "App/producto.html", {"formularioProducto":formularioProducto})

def descuento(request):
    if request.method =='POST':

        formularioDescuento= Descuento(request.POST)
        print(formularioDescuento)
        
        if formularioDescuento.is_valid:

            informacion= formularioDescuento.cleaned_data
            descuento= Descuento(descuento= informacion['descuento'],)

            descuento.save()

            return render(request, "App/inicio.html")

    else:
        formularioDescuento= Descuento()
    return render(request, "App/producto.html", {"formularioDescuento":formularioDescuento})

def buscarProducto(request):

    return render(request, "App/buscarProducto.html")
    
def buscar(request):
    if request.GET['nombre']:
        nombre= request.GET['nombre']
        producto= Producto.objects.filter(nombre__icontains=nombre)
        
        return render (request, "App/resultadoProducto.html", {"producto":producto} )
    else:
        return render(request, "App/BuscarProducto.html", {"error":"No se ingresó ningún nombre"})
    


def inicio(request):
    return render(request, "App/inicio.html")


