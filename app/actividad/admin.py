""" Configuraciones del Admin """
from django.contrib import admin

from .models import Clientes, Ordenes, Companias, Secciones, Productores, Polizas

class ClientesAdmin(admin.ModelAdmin):
    """ Clase con las configuraciones para el Admin de clientes """
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display = ['id', 'nombre', 'direccion']
    # añade un campo de texto para realizar la búsqueda, puedes añadir mas de un atributo
    search_fields = ['id', 'direccion', 'nombre']
    # añade una lista desplegable con la que podrás filtrar (activo es un atributo booleano)
    list_filter = ['status']

class CompaniasAdmin(admin.ModelAdmin):
    """ Clase con las configuraciones para el Admin de Companias """
    list_display = ['id', 'nombre', 'direccion']
    search_fields = ['id', 'direccion', 'nombre', 'razon_social']
    list_filter = ['status']

class OrdenesAdmin(admin.ModelAdmin):
    """ Clase con las configuraciones para el Admin de Ordenes """
    list_display = ['numero', 'orden_productor', 'vigencia_desde', 'vigencia_hasta', 'compania', 'cliente', 'productor']
    search_fields = ['numero', 'orden_productor', 'compania__nombre', 'cliente__nombre', 'productor__nombre']
    # list_filter = ['compania', 'cliente', 'productor']

class SeccionesAdmin(admin.ModelAdmin):
    """ Clase con las configuraciones para el Admin de Secciones """
    list_display = ['nombre', 'abrev']
    search_fields = ['nombre', 'abrev']

class ProductoresAdmin(admin.ModelAdmin):
    """ Clase con las configuraciones para el Admin de Productores """
    list_display = ['nombre', 'direccion']
    search_fields = ['nombre', 'direccion']

class PolizasAdmin(admin.ModelAdmin):
    """ Clase con las configuraciones para el Admin de Productores """
    list_display = ['numero', 'vigencia_desde', 'vigencia_hasta']
    search_fields = ['numero', 'vigencia_desde', 'vigencia_hasta']
    # search_fields = ['numero', 'vigencia_desde', 'vigencia_hasta', 'clientes__nombre', 'productor__nombre']

admin.site.site_header = "Asegurarse"
admin.site.site_title = "Panel de control"
 
# Register your models here.
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Ordenes, OrdenesAdmin)
admin.site.register(Companias, CompaniasAdmin)
admin.site.register(Secciones, SeccionesAdmin)
admin.site.register(Productores, ProductoresAdmin)
admin.site.register(Polizas, PolizasAdmin)

