from django.shortcuts import render, HttpResponse


def Inicio(request):
    
    return render(request, "bolicheapp/Inicio.html")




