""" Configuraciones del Admin """
from django.contrib import admin

from .models import LibrosRubricados, RegistrosLibros

admin.site.register(LibrosRubricados)
admin.site.register(RegistrosLibros)
