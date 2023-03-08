"""
Conjunto de funciones y métodos para la asistencia en el sistema
"""

from django.utils.html import format_html

FORMATO = "width=700,height=500,status=no,location=no,toolbar=no"


def get_button(esquema, modelo, param, titulo):
    """
    Función que arma el html para los botones de redireccion personalizados.
    Con los parametros recibidos arma un link a un listado dentro del sistema. 
    Ademas completa el parámetro de la búsqueda por la relación.

    El valor retornado sera del estilo:
    <input type="button" onclick="window.open('/admin/actividad/polizas/?q=
        ABRAMOVICH JIMENA&amp;_popup=1', 'Polizas cliente','width=500,height=500,
        status=no,location=no,toolbar=no')" value="Polizas cliente">

    """
    direccion = '/admin/'+esquema+'/'+modelo+'/?q='+param+'&amp;_popup=1'

    win = direccion+'\', \''+titulo+'\',\''+FORMATO
    to_format = get_button_link(win, titulo)

    return format_html(to_format)

def get_button_new(esquema, modelo, titulo):
    direccion = '/admin/'+esquema+'/'+modelo+'/add/'

    win = direccion+'\', \''+titulo+'\',\''+FORMATO
    to_format = get_button_link(win, titulo)

    return format_html(to_format)

def get_button_link(direccion, titulo):
    return '<input type="button" onclick="window.open(\''+direccion+'\')" value="'+titulo+'" />'