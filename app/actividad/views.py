from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .forms import CompaniaForm
from .models import Clientes, Companias, Secciones, Productores, Ordenes
from django.core.paginator import Paginator


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
