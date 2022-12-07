from django.shortcuts import render
from serviciosapp.models import Servicio
# Create your views here.

def Servicios(request):
    servicios=Servicio.objects.all()
    return render(request,"servicios/servicios.html", {"servicios": servicios})