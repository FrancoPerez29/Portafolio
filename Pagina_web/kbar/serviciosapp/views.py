from django.shortcuts import render
from serviciosapp.models import Servicio
# Create your views here.

def Servicios(request):
    Servicios=Servicio.objects.all()
    return render(request, "servicios/Servicios.html",{"servicios":Servicios})
