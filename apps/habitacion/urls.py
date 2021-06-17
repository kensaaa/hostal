from django.urls import path
from .views import *

urlpatterns = [
        path('crear-habitacion/',CrearHabitacion.as_view(),name= 'crear_habitacion'),
        path('lista-habitacion/',ListadoHabitacion.as_view(),name= 'listar_habitacion'),
        path('actualizar-habitacion/<int:pk>/',ActualizarHabitacion.as_view(),name= 'actualizar_habitacion')
]
