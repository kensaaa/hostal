from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from apps.compra.models import Orden_Compra
from .forms import *


class ListarOrdenCurso(ListView):
    model = Orden_Compra
    template_name = 'cliente/listar_curso.html'
    context_object_name = 'ordenes'
    queryset = Orden_Compra.objects.all()




class ListarPago(ListView):
    model = Orden_Compra
    template_name = 'cliente/listar_pago.html'
    context_object_name = 'ordenes'
    queryset = Orden_Compra.objects.filter(estado=True)





def solicitarOrden(request):

    data = {
            'form':SolicitarOrdenForm()
            }

    if request.method == 'POST':
        formulario = SolicitarOrdenForm(data=request.POST)

        if formulario.is_valid():
            print('el formulario esta todo correcto')








    return render(request,'cliente/crear_orden.html',data)
