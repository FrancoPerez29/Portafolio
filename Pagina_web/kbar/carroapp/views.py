from django.shortcuts import render
from .carro import Carro
from tiendaapp.models import Producto
from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request, producto_id):
    carro=carro(request)
    