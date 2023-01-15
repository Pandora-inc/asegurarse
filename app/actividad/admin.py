from django.contrib import admin

# Register your models here.
from .models import Clientes, ClientesMediosdepago, Tiposdoc, Companias, Secciones, Productores

class ClientesAdmin(admin.ModelAdmin):
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display=['status', 'nombre', 'descrip']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrará
    search_fields = ['descrip', 'nombre']
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    list_filter = ['nombre']

# Register your models here.
admin.site.register(Tiposdoc)
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(ClientesMediosdepago)
admin.site.register(Companias)
admin.site.register(Secciones)
admin.site.register(Productores)
