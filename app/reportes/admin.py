""" Configuraciones del Admin """
from django.contrib import admin
from reportes.models import LibrosRubricados, RegistrosLibros

class LibrosAdmin(admin.ModelAdmin):
    # añade un campo de texto para realizar la búsqueda, puedes añadir mas de un atributo
    search_fields = ['fecha', 'tipo', 'impresion']
    # añade una lista desplegable con la que podrás filtrar (activo es un atributo booleano)
    list_filter = ['activo']
    fieldsets = (
        (id, {
            'fields': ('nombre','fecha')
        }),
        (' ', {
            'fields': ('tipo', 'impresion')
        }),
        ('*', {
            'fields': ('fecha_desde', 'fecha_hasta', 'pagina_desde', 'pagina_hasta')
        }),
        # (None, {
        #     'fields': ('button_generar', 'button_imprimir')
        # })
    )
    readonly_fields = ('button_generar', 'button_imprimir')

    def button_imprimir(self, request):
        print("Aca se imprime en pdf")
    
    def button_generar(self, request):
        # return get_button("actividad", "polizas", request.nombre, "Polizas cliente")
        print("Aca se genera el libro")

admin.site.register(LibrosRubricados)
admin.site.register(RegistrosLibros)
