import imp
from django.urls import path
from App import views

urlpatterns = [
   path('usuario/', views.usuario),
]