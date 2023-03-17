from django.contrib import admin

# Register your models here.

from .models import *


class BancosucuInline(admin.TabularInline):
    model = Bancosucu

class BancoAdmin(admin.ModelAdmin):
    change_form_template = 'admin/new_change_form.html'
    """ Clase con las configuraciones para el Admin de Banco """
    list_display = ['descrip']
    search_fields = ['descrip']
    inlines = [BancosucuInline]


admin.site.register(Banco, BancoAdmin)
# admin.site.register(Bancosucu)
admin.site.register(Provincias)
admin.site.register(Postal)
admin.site.register(Monedas)
admin.site.register(Tipospedido)
admin.site.register(Tipospoliza)
admin.site.register(Mediosdepago)
