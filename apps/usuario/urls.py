from django.urls import path
from .views import *

urlpatterns = [
        path('listar-cliente/',ListarCliente.as_view(),name='listar_cliente'),
        path('crear-cliente/',CrearCliente.as_view(),name='crear_cliente'),
        path('actualizar-cliente/<int:pk>/',ActualizarCliente.as_view(),name='actualizar_cliente'),
        path('listar-proveedor/',ListarProveedor.as_view(),name='listar_proveedor'),
        path('crear-proveedor/',CrearProveedor.as_view(),name='crear_proveedor'),
        path('actualizar-proveedor/<int:pk>/',ActualizarProveedor.as_view(),name='actualizar_proveedor'),
        path('listar-empleado/',ListarEmpleado.as_view(),name='listar_empleado'),
        path('crear-empleado/',CrearEmpleado.as_view(),name='crear_empleado'),
        path('actualizar-empleado/<int:pk>/',ActualizarEmpleado.as_view(),name='actualizar_empleado'),
]
