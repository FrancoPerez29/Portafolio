from django.contrib import admin
from .models import Categoria, Post
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=("Created","updated")
    
class PostiaAdmin(admin.ModelAdmin):
    readonly_fields=("Created","updated")
    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostiaAdmin)