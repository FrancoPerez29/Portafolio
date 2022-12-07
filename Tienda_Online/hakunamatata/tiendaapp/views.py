from django.shortcuts import render
from .models import Producto

# Create your views here.


def Tienda(request):
    
    productos=Producto.objects.all()
    
    return render(request,"tiendaapp/tienda.html", {"productos":productos})