from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Banco)
admin.site.register(Bancosucu)
admin.site.register(Provincias)
admin.site.register(Postal)
admin.site.register(Monedas)
admin.site.register(Tipospedido)
admin.site.register(Tipospoliza)
admin.site.register(Mediosdepago)
