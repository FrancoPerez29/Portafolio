from email.headerregistry import ContentDispositionHeader
from django.contrib.auth.models import User
from tkinter import image_names
from django.db import models

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios')
    Created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
        
    def __str__(self):
        return self.titulo