""" Configuraciones del Admin """
from django.contrib import admin

from .models import Clientes, Ordenes, Companias, Secciones, Productores

class ClientesAdmin(admin.ModelAdmin):
    """ Clase con las configuraciones para el Admin de clientes """
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display = ['id', 'nombre', 'direccion']
    # añade un campo de texto para realizar la búsqueda, puedes añadir mas de un atributo
    search_fields = ['id', 'direccion', 'nombre']
    # añade una lista desplegable con la que podrás filtrar (activo es un atributo booleano)
    list_filter = ['status']

class ClientesCompanias(admin.ModelAdmin):
    """ Clase con las configuraciones para el Admin de Companias """
    list_display = ['id', 'nombre', 'direccion']
    search_fields = ['id', 'direccion', 'nombre', 'razon_social']
    list_filter = ['status']

class ClientesOrdenes(admin.ModelAdmin):
    """ Clase con las configuraciones para el Admin de Ordenes """
    list_display = ['numero', 'orden_productor', 'vigencia_desde', 'vigencia_hasta', 'compania', 'cliente', 'productor']
    search_fields = ['numero', 'compania__nombre', 'cliente__nombre', 'productor__nombre']
    # list_filter = ['compania', 'cliente', 'productor']

class ClientesSecciones(admin.ModelAdmin):
    """ Clase con las configuraciones para el Admin de Secciones """
    list_display = ['nombre', 'abrev']
    search_fields = ['nombre', 'abrev']

class ClientesProductores(admin.ModelAdmin):
    """ Clase con las configuraciones para el Admin de Productores """
    list_display = ['nombre', 'direccion']
    search_fields = ['nombre', 'direccion']


admin.site.site_header = "Asegurarse"
admin.site.site_title = "Panel de control"
 
# Register your models here.
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Ordenes, ClientesOrdenes)
admin.site.register(Companias, ClientesCompanias)
admin.site.register(Secciones, ClientesSecciones)
admin.site.register(Productores, ClientesProductores)

