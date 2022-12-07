from distutils.command.upload import upload
from mailbox import NoSuchMailboxError
from tabnanny import verbose
from turtle import update
from django.db import models

# Create your models here.
class CatergoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="categoriaprod"
        verbose_name_plural="categoriasprods"
        
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CatergoriaProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    precio=models.FloatField()
    stock=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name="producto"
        verbose_name_plural="productos"
    