from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from .models import *
from .forms import *


class CrearCompra(CreateView):
    model = Orden_Compra
    form_class = OrdenCompraForm
    template_name = 'compra/ordenCompra/crear_compra.html'
    success_url = reverse_lazy('compra:listar_compra')




class CrearHuesped(CreateView):
    model = Huesped
    form_class = HuespedForm
    template_name = 'compra/huesped/crear_huesped.html'
    success_url = reverse_lazy('compra:listar_huesped')




class CrearGasto(CreateView):
    model = Gasto_Huesped_Plato
    form_class = GastoForm
    template_name = 'compra/gastoHuesped/crear_gasto.html'
    success_url = reverse_lazy('compra:listar_gasto')








class ListarCompra(ListView):
    model = Orden_Compra
    template_name = 'compra/ordenCompra/listar_compra.html'
    context_object_name = 'compras'
    queryset = Orden_Compra.objects.all()




class ListarHuesped(ListView):
    model = Huesped
    template_name = 'compra/huesped/listar_huesped.html'
    context_object_name = 'huespedes'
    queryset = Huesped.objects.all()




class ListarGasto(ListView):
    model = Gasto_Huesped_Plato
    template_name = 'compra/gastoHuesped/listar_gasto.html'
    context_object_name = 'gastos'
    queryset = Gasto_Huesped_Plato.objects.all()








class ActualizarCompra(UpdateView):
    model = Orden_Compra
    form_class = OrdenCompraForm
    template_name = 'compra/ordenCompra/actualizar_compra.html'
    success_url = reverse_lazy('compra:listar_compra')




class ActualizarHuesped(UpdateView):
    model = Huesped
    form_class = HuespedForm
    template_name = 'compra/huesped/actualizar_huesped.html'
    success_url = reverse_lazy('compra:listar_huesped')




class ActualizarGasto(UpdateView):
    model = Gasto_Huesped_Plato
    form_class = GastoForm
    template_name = 'compra/gastoHuesped/actualizar_gasto.html'
    success_url = reverse_lazy('compra:listar_gasto')
