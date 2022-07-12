

from django.urls import path
from App import views

urlpatterns = [
   path('usuario/', views.usuario, name="usuario"),
   path('inicio/', views.inicio, name="inicio"),
   path('producto/', views.producto, name="producto"),
]