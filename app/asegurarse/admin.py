from django.contrib import admin

admin.site.site_header = 'Mi sitio web de Django'
admin.site.site_title = 'Mi sitio web de Django'

class MiAdminSite(admin.AdminSite):
    site_header = 'Mi sitio web de Django'
    site_title = 'Mi sitio web de Django'
    index_title = 'Bienvenido al panel de administración de Mi sitio web de Django'

    # Definir el orden del menú de administración
    order = (
        ('Actividad', {
            'models': (
                'actividad.Clientes',
                'actividad.Ordenes',
                'actividad.Polizas',
                'actividad.Comprobantes',
                'actividad.Cheques',
                'actividad.Rendiciones',
                'actividad.Companias',
                'actividad.Secciones',
                'actividad.Productores',
            )
        }),
        # ('Contenido', {
        #     'models': (
        #         'miapp.Articulo',
        #         'miapp.Comentario'
        #     )
        # }),
        # ('Opciones avanzadas', {
        #     'models': (
        #         'miapp.Configuracion',
        #         'miapp.Notificacion'
        #     )
        # }),
    )

admin_site = MiAdminSite()