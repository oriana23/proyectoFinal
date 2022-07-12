from django import http
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from App.models import *

def usuario(request):
    return render(request, "App/usuario.html")



