from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import ListarCompanias, AgregarCompania, EliminarCompania, EditarCompania, listarOrdenes, ListarOrdenes

urlpatterns = [
    path('', views.actividad, name='actividad'),
    path('clientes/', views.clientes, name='clientes'),

    path('ordenes/', login_required(ListarOrdenes.as_view()), name='ordenes'),

    path('companias/', login_required(ListarCompanias.as_view()), name='companias'),
    path('companias/agregar/', login_required(AgregarCompania.as_view()), name='agregarcompania'),
    path('companias/eliminar/<int:pk>', login_required(EliminarCompania.as_view()), name='eliminarcompania'),
    path('companias/editar/<int:pk>', login_required(EditarCompania.as_view()), name='editarcompania'),

    path('secciones/', views.secciones, name='secciones'),
    path('productores/', views.productores, name='productores'),
]
app_name='actividad'

