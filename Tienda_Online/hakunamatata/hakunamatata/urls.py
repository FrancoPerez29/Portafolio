"""hakunamatata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('hakunamatataapp.urls')),
    path('servicios/', include('serviciosapp.urls')),
    path('noticias/', include('noticiasapp.urls')),
    path('contacto/', include('contactoapp.urls')),
    path('tienda/', include('tiendaapp.urls')),
    path('carro/', include('carroapp.urls')),
    path('autenticacion/', include('autenticacionapp.urls')),
    path('pedidos/', include('pedidosapp.urls')),
]