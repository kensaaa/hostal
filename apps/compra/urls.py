from django.urls import path
from .views import *

urlpatterns = [
        path('crear-compra/',CrearCompra.as_view(),name='crear_compra'),
        path('listar-compra/',ListarCompra.as_view(),name='listar_compra'),
        path('actualizar-compra/<int:pk>/',ActualizarCompra.as_view(),name='actualizar_compra'),
        path('crear-huesped/',CrearHuesped.as_view(),name='crear_huesped'),
        path('listar-huesped/',ListarHuesped.as_view(),name='listar_huesped'),
        path('actualizar-huesped/<int:pk>/',ActualizarHuesped.as_view(),name='actualizar_huesped'),
        path('crear-gasto/',CrearGasto.as_view(),name='crear_gasto'),
        path('listar-gasto/',ListarGasto.as_view(),name='listar_gasto'),
        path('actualizar-gasto/<int:pk>/',ActualizarGasto.as_view(),name='actualizar_gasto'),
]
