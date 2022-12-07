from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class CategoriaProducto(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="categoriaproducto"
        verbose_name_plural="categoriaproductos"
        
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda", null=True,blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name="producto"
        verbose_name_plural="productos"
        
        