from django.urls import path
from .views import *

urlpatterns = [
        path('orden-curso/',ListarOrdenCurso.as_view(),name='listar_curso'),
        path('orden-pago/',ListarPago.as_view(),name='listar_pago'),
        path('solicitar-orden/',solicitarOrden,name='solicitar_orden'),
]
