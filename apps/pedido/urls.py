from django.urls import path
from .views import *

urlpatterns = [
        path('crear-pedido/',CrearOrdenPedido.as_view(),name='crear_pedido'),
        path('crear-detalle/',CrearDetallePedido.as_view(),name='crear_detalle'),
        path('crear-producto/',CrearProducto.as_view(),name='crear_producto'),
        path('listar-pedido/',ListarOrdenPedido.as_view(),name='listar_pedido'),
        path('listar-detalle/',ListarDetallePedido.as_view(),name='listar_detalle'),
        path('listar-producto/',ListarProducto.as_view(),name='listar_producto'),
        path('actualizar-pedido/<int:pk>/',ActualizarOrdenPedido.as_view(),name='actualizar_pedido'),
        path('actualizar-detalle/<int:pk>/',ActualizarDetallePedido.as_view(),name='actualizar_detalle'),
        path('actualizar-producto/<int:pk>/',ActualizarProducto.as_view(),name='actualizar_producto'),
]
