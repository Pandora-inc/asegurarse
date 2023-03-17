from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.core.paginator import Paginator
from django.utils import timezone
from django.db import connection

from .forms import ClientesPolizasForm, CompaniaForm, LibrosRubricadosForm, VencimientoPolizasForm
from .models import Clientes, Companias, Secciones, Productores, Ordenes, Polizas


# Create your views here.


def actividad(request):
    return render(request, "panel.html", {'navbar': 'actividad'})


@login_required(login_url='login')
def clientes(request):
    lista_clientes = Clientes.objects.all()
    paginator = Paginator(lista_clientes, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'clientes.html', {
        'lista_clientes': page_obj,
        'col': 1
    })


def listarOrdenes(request):
    ordenes = Ordenes.objects.select_related('cliente').order_by('-numero').only(
        "numero", "orden_productor", "cliente", "vigencia_desde", "vigencia_hasta",
        "compania", "cliente", "productor"
    )
    paginator = Paginator(ordenes, ordenes.count())

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ordenes.html', {
        'ordenes': page_obj,
        'col': 3
    })


class ListarOrdenes(ListView):
    template_name = 'ordenes.html'
    context_object_name = 'ordenes'
    queryset = Ordenes.objects.select_related('cliente').order_by('-numero').only(
        "numero", "orden_productor", "cliente", "vigencia_desde", "vigencia_hasta",
        "compania", "cliente", "productor"
    )
    paginate_by = 7


class ListarCompanias(ListView):
    template_name = 'companias.html'
    context_object_name = 'companias'
    queryset = Companias.objects.all()


class AgregarCompania(CreateView):
    model = Companias
    form_class = CompaniaForm
    template_name = 'actividad/companias/agregar-compania.html'
    success_url = reverse_lazy('actividad:companias')


class EliminarCompania(DeleteView):
    model = Companias

    def post(self, request, pk, *args, **kwargs):
        compania = Companias.objects.get(id=pk)
        compania.delete()
        return redirect('/actividad/companias')


class EditarCompania(UpdateView):
    model = Companias
    template_name = 'actividad/companias/editar-compania.html'
    form_class = CompaniaForm
    success_url = reverse_lazy('actividad:companias')


@login_required(login_url='login')
def secciones(request):
    lista_secciones = Secciones.objects.all()
    paginator = Paginator(lista_secciones, lista_secciones.count())

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'secciones.html', {
        'lista_secciones': page_obj,
        'col': 0
    })


@login_required(login_url='login')
def productores(request):
    lista_productores = Productores.objects.all()
    paginator = Paginator(lista_productores, lista_productores.count())

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'productores.html', {
        'lista_productores': page_obj,
        'col': 0
    })


def vencimiento_polizas(request):
    if request.method == "POST":
        form = VencimientoPolizasForm(request.POST)
        # fields = ("productor", "seccion", "vigencia_desde", "vigencia_hasta")
        # seccion = request.seccion

        if form.is_valid():
            productor = request.POST.get('productor', '*')
            seccion = request.POST.get('seccion', '*')
            vigencia_desde = request.POST.get('vigencia_desde', '*')
            vigencia_hasta = request.POST.get('vigencia_hasta', timezone.now())

            q = {}

            if vigencia_hasta:
                q['vigencia_hasta__lte'] = vigencia_hasta
            else:
                vigencia_hasta = timezone.now()
                q['vigencia_hasta__lte'] = vigencia_hasta

            if vigencia_desde:
                q['vigencia_desde'] = vigencia_desde

            if seccion:
                q['seccion'] = seccion

            if productor:
                q['productor'] = productor

            polizas = Polizas.objects.filter(**q).order_by('vigencia_hasta')
            return render(request, 'polizas_vto.html', {'polizas': polizas})
    else:
        form = VencimientoPolizasForm()
        return render(request, 'form_polizas_vto.html', {'form': form})


def cliente_polizas(request):
    if request.method == "POST":
        form = ClientesPolizasForm(request.POST)

        if form.is_valid():
            cliente = request.POST.get('cliente', '*')
            seccion = request.POST.get('seccion', '*')
            vigencia_desde = request.POST.get('vigencia_desde', '*')
            vigencia_hasta = request.POST.get('vigencia_hasta', timezone.now())

            q = {}

            if vigencia_hasta:
                q['vigencia_hasta__lte'] = vigencia_hasta
            else:
                vigencia_hasta = timezone.now()
                q['vigencia_hasta__lte'] = vigencia_hasta

            if vigencia_desde:
                q['vigencia_desde'] = vigencia_desde

            if seccion:
                q['seccion'] = seccion

            if cliente:
                q['cliente'] = cliente

            polizas = Polizas.objects.filter(**q).order_by('vigencia_hasta')
            return render(request, 'polizas_cliente.html', {'polizas': polizas})
    else:
        form = ClientesPolizasForm()
        return render(request, 'form_polizas_cliente.html', {'form': form})


def libros_rubricados(request):
    """Libros rubricados"""
    if request.method == "POST":
        form = LibrosRubricadosForm(request.POST)

        if form.is_valid():

            if int(request.POST.get('encRubr')) == 2:
                if int(request.POST.get('rendOp')) == 1:
                    ordenes = recuperar_rubri_rendiciones(request.POST.get(
                        'vigencia_desde'), request.POST.get('vigencia_hasta'))
                else:
                    ordenes = recuperar_rubri_operaciones(request.POST.get(
                        'vigencia_desde'), request.POST.get('vigencia_hasta'))
                    

            return render(request, 'libros_rubricados.html', {'ordenes': ordenes})
    else:
        form = LibrosRubricadosForm()
        return render(request, 'form_libros.html', {'form': form})

def recuperar_rubri_operaciones(fecha_desde, fecha_hasta):
    with connection.cursor() as cursor:
        print(fecha_desde, fecha_hasta)
        sql = "SELECT ordenes.numero, polizas.fecha, polizas.vigencia_desde, polizas.vigencia_hasta, polizas.prima, clientes.nombre, clientes.direccion, companias.nombre, ordenes.direccion, ordenes.riesgo_desc, secciones.nombre, 'observaciones' FROM     polizas, ordenes, clientes, companias, secciones WHERE polizas.fecha BETWEEN '"+fecha_desde+"' AND '"+fecha_hasta+"' AND polizas.id = ordenes.poliza_id AND polizas.cliente_id = clientes.id AND polizas.compania_id = companias.id AND polizas.seccion_id = secciones.id ORDER BY polizas.fecha"
    
        cursor.execute(sql)
        ordenes = cursor.fetchall()

        print(ordenes)
        return ordenes

def recuperar_rubri_rendiciones(fecha_desde, fecha_hasta):
    with connection.cursor() as cursor:
        sql = "SELECT 1, pagos_cuotas.fecha, polizas.numero, companias.nombre, pagos_cuotas.importe, 0, cuotas_polizas.nro_cuota, polizas.cant_cuotas FROM polizas, companias, cuotas_polizas, pagos_cuotas WHERE polizas.id = cuotas_polizas.poliza_id AND cuotas_polizas.id = pagos_cuotas.cuota_id AND polizas.compania_id = companias.id AND pagos_cuotas.fecha BETWEEN '%s' AND '%s' UNION SELECT 2, rendiciones.fecha, polizas.numero, companias.nombre, 0, SUM(pagos_cuotas.importe), cuotas_polizas.nro_cuota, polizas.cant_cuotas FROM rendiciones, polizas, companias, pagos_cuotas, cuotas_polizas WHERE rendiciones.cuota_id = cuotas_polizas.id AND rendiciones.poliza_id = polizas.id AND polizas.id = cuotas_polizas.poliza_id AND cuotas_polizas.id = pagos_cuotas.cuota_id AND polizas.compania_id = companias.id AND rendiciones.fecha BETWEEN '%s' AND '%s' ORDER BY 2"

        cursor.execute(sql, (
            fecha_desde,
            fecha_hasta,
            fecha_desde,
            fecha_hasta))
        
        row = cursor.fetchall()
    return row
