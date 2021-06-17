from django.urls import path
from .views import *

urlpatterns = [
        path('listar-plato/',ListarPlato.as_view(),name='listar_plato'),
        path('crear-plato/',CrearPlato.as_view(),name='crear_plato'),
        path('actualizar-plato/<int:pk>/',ActualizarPlato.as_view(),name='actualizar_plato'),
]
