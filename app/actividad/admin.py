""" Configuraciones del Admin """
import datetime
import logging
from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html
from django.urls import path
from django.urls.base import reverse

from .forms import PolizasCustomForm

from .actions import get_button, get_button_new
from .models import Cheques, Clientes, Comprobantes, Cuotas, Ordenes, Companias, Pagos, Rendiciones, Secciones, Productores, Polizas, ClientesMediosdepago


class ClientesMediosdepagoInline(admin.TabularInline):
    model = ClientesMediosdepago
    extra = 0


class OrdenesInline(admin.TabularInline):
    model = Ordenes
    extra = 0


class PolizasInline(admin.TabularInline):
    model = Polizas
    extra = 0


class CompaniasInline(admin.TabularInline):
    model = Companias
    extra = 0


class ClientesAdmin(admin.ModelAdmin):
    """ Clase con las configuraciones para el Admin de clientes """
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display = ['id', 'nombre', 'direccion']
    # añade un campo de texto para realizar la búsqueda, puedes añadir mas de un atributo
    search_fields = ['id', 'direccion', 'nombre']
    # añade una lista desplegable con la que podrás filtrar (activo es un atributo booleano)
    list_filter = ['activo']
    fieldsets = (
        (id, {
            'fields': ('button_polizas', 'button_ordenes', 'button_estado_cuenta', 'button_pagos', 'button_cheques')
        }),
        ('Datos Personales', {
            'fields': ('nombre', 'direccion', 'postal', 'telefonos', 'email', 'tipodoc', 'documento', 'cuit', 'nacimiento', 'actividad')
        }),
        (' ', {
            'fields': ('fecha', 'productor', 'seg_retiro', 'corresp')
        }),
        ('Informacion Bancaria', {
            'fields': ('banco', 'banco_suc', 'banco_caja', 'banco_ctacte', 'debaut')
        }),
        ('Registro', {
            'fields': ('reg_num', 'reg_categ', 'reg_juris', 'reg_venc')
        }),
        ('Observaciones', {
            'fields': ('observaciones', 'activo')
        }),
        (None, {
            'fields': ('zona_cza', 'fuente', 'descrip', 'establecim')
        })
    )
    inlines = [ClientesMediosdepagoInline, OrdenesInline, PolizasInline]
    readonly_fields = ('button_polizas', 'button_ordenes',
                       'button_estado_cuenta', 'button_pagos', 'button_cheques')

    def button_polizas(self, request):
        return get_button("actividad", "polizas", request.nombre, "Polizas cliente")

    def button_ordenes(self, request):
        return get_button("actividad", "ordenes", request.nombre, "Ordenes cliente")

    def button_estado_cuenta(self, request):
        return get_button("actividad", "cuotas", request.nombre, "Estado de cuenta")

    def button_pagos(self, request):
        return get_button("actividad", "pagos", request.nombre, "Pagos realizados")

    def button_cheques(self, request):
        return get_button_new("actividad", "cheques", "Ingresar cheque")


class CompaniasAdmin(admin.ModelAdmin):
    """ Clase con las configuraciones para el Admin de Companias """
    list_display = ['id', 'nombre', 'direccion']
    search_fields = ['id', 'direccion', 'nombre', 'razon_social']
    list_filter = ['status']
    # inlines = [CompaniasInline]


class OrdenesAdmin(admin.ModelAdmin):
    """ Clase con las configuraciones para el Admin de Ordenes """
    list_display = ['numero', 'orden_productor', 'vigencia_desde',
                    'vigencia_hasta', 'compania', 'cliente', 'productor']
    search_fields = ['numero', 'orden_productor',
                     'compania__nombre', 'cliente__nombre', 'productor__nombre']
    # list_filter = ['compania', 'cliente', 'productor']
    fieldsets = (
        ('Orden', {
            'fields': ('numero', 'orden_productor', 'fecha', 'cliente', 'productor', 'cod_productor', 'organizador')
        }),
        ('Riesgo', {
            'fields': ('direccion', 'postal', 'localidad', 'riesgo_desc')
        }),
        ('Vigencia', {
            'fields': ('vigencia_desde', 'vigencia_hasta')
        }),
        ('Forma de pago', {
            'fields': ('mediodepago', 'nro_mediopago', 'responsable')
        }),
        ('Poliza solicitada', {
            'fields': ('tipopoliza', 'num_poliza_ref', 'seccion', 'cobertura', 'compania', 'moneda')
        }),
        ('Comisiones', {
            'fields': ('produccion', 'cobranza', 'recup_gastos')
        }),
        ('Valores', {
            'fields': ('suma', 'prima', 'recargos', 'bonificacion', 'premio')
        }),
        ('Poliza emitida', {
            'fields': ('poliza', 'flag')
        }),
        (None, {
            'fields': ('bien_asegurado', 'riesgo_valor', 'codigo_productor', 'status')
        }),
    )


class SeccionesAdmin(admin.ModelAdmin):
    """ Clase con las configuraciones para el Admin de Secciones """
    list_display = ['nombre', 'abrev']
    search_fields = ['nombre', 'abrev']


class ProductoresAdmin(admin.ModelAdmin):
    """ Clase con las configuraciones para el Admin de Productores """
    list_display = ['nombre', 'direccion']
    search_fields = ['nombre', 'direccion']
    inlines = [CompaniasInline]


class PolizasAdmin(admin.ModelAdmin):
    """ Clase con las configuraciones para el Admin de Productores """
    list_display = ['numero', 'vigencia_desde', 'vigencia_hasta']
    search_fields = ['numero', 'cliente__nombre',
                     'vigencia_desde', 'vigencia_hasta']
    fieldsets = (
        ('Orden', {
            'fields': ('numero', 'cliente', 'productor', 'organizador')
        }),
        ('Vigencia', {
            'fields': ('vigencia_desde', 'vigencia_hasta')
        }),
        ('Riesgo', {
            'fields': ('direccion', 'postal', 'provincia')
        }),
        ('Poliza', {
            'fields': ('num_poliza', 'fecha', 'tipopoliza', 'seccion', 'cobertura', 'compania', 'moneda')
        }),
        ('Siniestros', {
            'fields': ('siniestro01', 'siniestro02', 'siniestro03', 'siniestro04')
        }),
        ('valores', {
            'fields': ('suma', 'prima', 'recargos', 'bonificacion', 'premio')
        }),
        ('Comisiones', {
            'fields': ('produccion', 'cobranza', 'recup_gastos')
        }),
        ('???', {
            'fields': ('fecha_recepcion', 'iva', 'ing_brutos')
        }),
        ('Formas de pago', {
            'fields': ('mediodepago', 'nro_mediopago', 'cant_cuotas')
        }),
        (None, {
            'fields': ('bien_asegurado', 'riesgo_desc', 'status')
        }),
        ('.', {
            'fields': ('riesgo_valor', 'email', 'nota_credito', 'telefonos', 'restante')
        }),
    )


class CuotasAdmin(admin.ModelAdmin):

    list_display = ['fecha_venc', 'poliza', 'nro_cuota',
                    'get_cuotas', 'importe', 'saldo', 'get_estado']
    search_fields = ['fecha_venc', 'poliza__numero', 'nro_cuota',
                     'poliza_id__cliente__nombre', 'poliza_id__cant_cuotas', 'importe', 'saldo']

    def get_estado(self, obj):
        # TODO Aca debe duscar el numero de cueto dentro de la tabla pagos para asegurarse de si esta paga
        return "En termino" if obj.fecha_venc > datetime.date.today() else "Vencida"

    def get_cuotas(self, obj):
        return obj.poliza.cant_cuotas


class PagosAdmin(admin.ModelAdmin):

    list_display = ['get_vencimiento', 'get_poliza',
                    'cuota', 'get_cuotas', 'importe']
    search_fields = ['cuota__poliza_id__cliente__nombre']

    def get_poliza(self, obj):
        return obj.cuota.poliza

    def get_vencimiento(self, obj):
        return obj.cuota.fecha_venc

    def get_cuotas(self, obj):
        return str(obj.cuota.nro_cuota) + " / " + str(obj.cuota.poliza.cant_cuotas)


class ChequesAdmin(admin.ModelAdmin):

    list_display = ['cliente', 'fecha', 'numero', 'valor', 'banco', 'sucursal']
    search_fields = ['cliente__nombre', 'numero', 'fecha']


class ComprobantesAdmin(admin.ModelAdmin):

    list_display = ['numero', 'cliente', 'fecha', 'valor', 'restante', 'tipo']
    search_fields = ['numero', 'fecha', 'valor',
                     'restante', 'tipo__descrip', 'cliente__nombre']


class RendicionesAdmin(admin.ModelAdmin):

    list_display = ['fecha', 'productor', 'fecha_cierre', 'total', 'compania']
    search_fields = ['fecha', 'productor__nombre',
                     'fecha_cierre', 'total', 'compania__nombre']


class NuevoPolizasAdmin(admin.ModelAdmin):
    form = PolizasCustomForm

    ordering = ['numero']
    list_display = ['numero', 'vigencia_desde', 'vigencia_hasta']
    search_fields = ['numero', 'cliente__nombre',
                     'vigencia_desde', 'vigencia_hasta']


class MyModelAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('my_view/', self.admin_site.admin_view(self.my_view), name='my_view'),
        ]
        return my_urls + urls

    def my_view(self, request):
        # Aquí puedes escribir tu vista personalizada
        # Por ejemplo, puedes renderizar una plantilla HTML
        return HttpResponse("¡Hola desde mi vista personalizada!")

    def my_view_link(self):
        # Define el enlace y su etiqueta personalizada
        url = reverse('admin:my_view')
        return format_html('<a href="{}">Mi vista personalizada</a>', url)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['my_view_link'] = self.my_view_link()
        return super().change_view(request, object_id, form_url, extra_context=extra_context)


admin.site.site_header = "Asegurarse"
admin.site.site_title = "Panel de control"

# Register your models here.
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Ordenes, OrdenesAdmin)
admin.site.register(Companias, CompaniasAdmin)
admin.site.register(Secciones, SeccionesAdmin)
admin.site.register(Productores, ProductoresAdmin)
# admin.site.register(Polizas, PolizasAdmin)
admin.site.register(Cuotas, CuotasAdmin)
admin.site.register(Pagos, PagosAdmin)
admin.site.register(Cheques, ChequesAdmin)
admin.site.register(Comprobantes, ComprobantesAdmin)
admin.site.register(Rendiciones, RendicionesAdmin)
admin.site.register(Polizas, NuevoPolizasAdmin) 
# admin.site.register(MyModelAdmin)

# admin.site.unregister(Cuotas)
