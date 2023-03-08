from django.urls import include, path
from . import views

urlpatterns = [
    path(r'^actividad/polizas/reporte/$', views.vencimiento_polizas),
    # path(r'^admin/', include('admin.site.urls')),
    # path('', views.post_list, name='post_list'),
]
