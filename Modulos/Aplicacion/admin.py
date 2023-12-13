from django.contrib import admin
from Modulos.Aplicacion.models import *

# Register your models here.

admin.site.register(estudiante)
admin.site.register(academico)
admin.site.register(administrativo)
admin.site.register(libro)
admin.site.register(prestamo)