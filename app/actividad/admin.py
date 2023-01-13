from django.contrib import admin

# Register your models here.
from .models import Clientes, ClientesMediosdepago, Tiposdoc, Companias, Secciones, Productores

# Register your models here.
admin.site.register(Tiposdoc)
admin.site.register(Clientes)
admin.site.register(ClientesMediosdepago)
admin.site.register(Companias)
admin.site.register(Secciones)
admin.site.register(Productores)
