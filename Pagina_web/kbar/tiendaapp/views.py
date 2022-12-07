from django.shortcuts import render
from .models import Producto

# Create your views here.

def Tienda(request):
    producto=Producto.objects.all()
    return render(request, "tienda/Tienda.html", {"productos": producto})
