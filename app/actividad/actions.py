"""
Conjunto de funciones y métodos para la asistencia en el sistema
"""

from django.utils.html import format_html


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
    formato = "width=500,height=600,status=no,location=no,toolbar=no"
    direccion = '/admin/'+esquema+'/'+modelo+'/?q='+param+'&amp;_popup=1'

    win = direccion+'\', \''+titulo+'\',\''+formato
    to_format = '<input type="button" onclick="window.open(\''+win+'\')" value="'+titulo+'" />'

    return format_html(to_format)
