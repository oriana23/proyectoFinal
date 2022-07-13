

from django.urls import path
from App.views import *

urlpatterns = [
   path('usuario/', usuario, name="usuario"),
   path('inicio/', inicio, name="inicio"),
   path('producto/', producto, name="producto"),
   path('descuento/', descuento, name="descuento"),
   path('buscar/', buscar, name="buscar"),
   path('buscarProducto/', buscarProducto, name="buscarProducto"),

   
]