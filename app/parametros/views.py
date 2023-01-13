from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, UpdateView, ListView

from .models import Banco, Postal, Monedas, Tipospedido, Tipospoliza, Mediosdepago
from .forms import TiposPedidoForm, TiposPolizaForm, MediosDePagoForm, MonedasForm, PostalForm


# Create your views here.


def parametros(request):
    return render(request, "panel.html", {'navbar': 'parametros'})


@login_required(login_url='login')
def banco(request):
    lista_bancos = Banco.objects.all()
    paginator = Paginator(lista_bancos, lista_bancos.count())

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bancos.html', {
        'lista_bancos': page_obj,
        'col': 0
    })

"""
    Views Postal
"""
class ListarPostal(ListView):
    template_name = 'postal.html'
    context_object_name = 'postales'
    queryset =  Postal.objects.select_related('provincia').all()
    paginate_by = 7

class AgregarPostal(CreateView):
    model = Postal
    form_class = PostalForm
    template_name = 'parametros/postal/agregar-postal.html'
    success_url = reverse_lazy('parametros:postal')

class EliminarPostal(DeleteView):
    model = Postal

    def post(self, request, pk, *args, **kwargs):
        postal = Postal.objects.get(id=pk)
        postal.delete()
        return redirect('/parametros/postal')

class EditarPostal(UpdateView):
    model = Postal
    template_name = 'parametros/postal/editar-postal.html'
    form_class = PostalForm
    success_url = reverse_lazy('parametros:postal')

"""
    Views Monedas
"""
class ListarMonedas(ListView):
    template_name = 'monedas.html'
    context_object_name = 'monedas'
    queryset = Monedas.objects.all()

class AgregarMoneda(CreateView):
    model = Monedas
    form_class = MonedasForm
    template_name = 'parametros/monedas/agregar-moneda.html'
    success_url = reverse_lazy('parametros:monedas')

class EliminarMoneda(DeleteView):
    model = Monedas

    def post(self, request, pk, *args, **kwargs):
        moneda = Monedas.objects.get(id=pk)
        moneda.delete()
        return redirect('/parametros/monedas')

class EditarMoneda(UpdateView):
    model = Monedas
    template_name = 'parametros/monedas/editar-moneda.html'
    form_class = MonedasForm
    success_url = reverse_lazy('parametros:monedas')


"""
    Views Tipos de Pedidos
"""
class ListarTiposPedido(ListView):
    template_name = 'tipos-pedido.html'
    context_object_name = 'tipospedidos'
    queryset = Tipospedido.objects.all()

class AgregarTipoPedido(CreateView):
    model = Tipospedido
    form_class = TiposPedidoForm
    template_name = 'parametros/tipospedido/agregar-tipo-pedido.html'
    success_url = reverse_lazy('parametros:tipospedido')

class EliminarTipoPedido(DeleteView):
    model = Tipospedido

    def post(self, request, pk, *args, **kwargs):
        tipopedido = Tipospedido.objects.get(id=pk)
        tipopedido.delete()
        return redirect('/parametros/tipospedido')

class EditarTipoPedido(UpdateView):
    model = Tipospedido
    template_name = 'parametros/tipospedido/editar-tipo-pedido.html'
    form_class = TiposPedidoForm
    success_url = reverse_lazy('parametros:tipospedido')


"""
    Views Tipos de Poliza
"""
class ListarTiposPoliza(ListView):
    template_name = 'tipos-poliza.html'
    context_object_name = 'tipospoliza'
    queryset = Tipospoliza.objects.all()


class AgregarTipoPoliza(CreateView):
    model = Tipospoliza
    form_class = TiposPolizaForm
    template_name = 'parametros/tipospoliza/agregar-tipo-poliza.html'
    success_url = reverse_lazy('parametros:tipospoliza')

class EliminarTipoPoliza(DeleteView):
    model = Tipospoliza

    def post(self, request, pk, *args, **kwargs):
        tipopoliza = Tipospoliza.objects.get(id=pk)
        tipopoliza.delete()
        return redirect('/parametros/tipospoliza')

class EditarTipoPoliza(UpdateView):
    model = Tipospoliza
    template_name = 'parametros/tipospoliza/editar-tipo-poliza.html'
    form_class = TiposPolizaForm
    success_url = reverse_lazy('parametros:tipospoliza')

"""
    Views Medios de Pago
"""
class ListarMediosDePago(ListView):
    template_name = 'medios-de-pago.html'
    context_object_name = 'mediosdepago'
    queryset = Mediosdepago.objects.all()


class AgregarMedioDePago(CreateView):
    model = Mediosdepago
    form_class = MediosDePagoForm
    template_name = 'parametros/mediosdepago/agregar-medio-de-pago.html'
    success_url = reverse_lazy('parametros:mediosdepago')

class EliminarMedioDePago(DeleteView):
    model = Mediosdepago

    def post(self, request, pk, *args, **kwargs):
        mediodepago = Mediosdepago.objects.get(id=pk)
        mediodepago.delete()
        return redirect('/parametros/mediosdepago')

class EditarMedioDePago(UpdateView):
    model = Mediosdepago
    template_name = 'parametros/mediosdepago/editar-medio-de-pago.html'
    form_class = MediosDePagoForm
    success_url = reverse_lazy('parametros:mediosdepago')
