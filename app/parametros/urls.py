from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import EliminarTipoPedido, AgregarTipoPedido, EditarTipoPedido, ListarTiposPedido, ListarTiposPoliza, \
    AgregarTipoPoliza, EliminarTipoPoliza, EditarTipoPoliza, ListarMediosDePago, AgregarMedioDePago, \
    EliminarMedioDePago, EditarMedioDePago, ListarMonedas, AgregarMoneda, EliminarMoneda, EditarMoneda, ListarPostal, \
    AgregarPostal, EliminarPostal, EditarPostal

app_name='parametros'
urlpatterns = [
    path('', views.parametros, name='parametros'),

    path('bancos/', views.banco, name='banco'),

    path('postal/', login_required(ListarPostal.as_view()), name='postal'),
    path('postal/agregar/', login_required(AgregarPostal.as_view()), name='agregarpostal'),
    path('postal/eliminar/<int:pk>', login_required(EliminarPostal.as_view()), name='eliminarpostal'),
    path('postal/editar/<int:pk>', login_required(EditarPostal.as_view()), name='editarpostal'),

    path('monedas/', login_required(ListarMonedas.as_view()), name='monedas'),
    path('monedas/agregar/', login_required(AgregarMoneda.as_view()), name='agregarmoneda'),
    path('monedas/eliminar/<int:pk>', login_required(EliminarMoneda.as_view()), name='eliminarmoneda'),
    path('monedas/editar/<int:pk>', login_required(EditarMoneda.as_view()), name='editarmoneda'),

    path('tipospedido/', login_required(ListarTiposPedido.as_view()), name='tipospedido'),
    path('tipospedido/agregar/', login_required(AgregarTipoPedido.as_view()), name='agregartipopedido'),
    path('tipospedido/eliminar/<int:pk>', login_required(EliminarTipoPedido.as_view()), name='eliminartipopedido'),
    path('tipospedido/editar/<int:pk>', login_required(EditarTipoPedido.as_view()), name='editartipopedido'),

    path('tipospoliza/', login_required(ListarTiposPoliza.as_view()), name='tipospoliza'),
    path('tipospoliza/agregar/', login_required(AgregarTipoPoliza.as_view()), name='agregartipopoliza'),
    path('tipospoliza/eliminar/<int:pk>', login_required(EliminarTipoPoliza.as_view()), name='eliminartipopoliza'),
    path('tipospoliza/editar/<int:pk>', login_required(EditarTipoPoliza.as_view()), name='editartipopoliza'),

    path('mediosdepago/', login_required(ListarMediosDePago.as_view()), name='mediosdepago'),
    path('mediosdepago/agregar/', login_required(AgregarMedioDePago.as_view()), name='agregarmediodepago'),
    path('mediosdepago/eliminar/<int:pk>', login_required(EliminarMedioDePago.as_view()), name='eliminarmediodepago'),
    path('mediosdepago/editar/<int:pk>', login_required(EditarMedioDePago.as_view()), name='editarmediodepago'),

]

