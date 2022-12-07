from django.contrib import admin
from django.contrib.auth.models import User

from .models import Servicio

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=("Created","updated")

admin.site.register(Servicio, ServicioAdmin)