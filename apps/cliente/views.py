from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from apps.compra.models import Orden_Compra,Huesped
from apps.habitacion.models import Tipo_Habitacion
from apps.comedor.models import Tipo_Comedor
from .models import Listado_Trabajador
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




def crearTrabajador(request,id):

    data = {
            'form':TrabajadorForm()
            }

    if request.method == 'POST':
        formulario = TrabajadorForm(data=request.POST)
        if formulario.is_valid():
            rut = formulario.cleaned_data['rut']
            nombres = formulario.cleaned_data['nombres']
            apaterno = formulario.cleaned_data['apaterno']
            amaterno = formulario.cleaned_data['amaterno']
            celular = formulario.cleaned_data['celular']
            tipo_comedor = Tipo_Comedor.objects.get(descripcion='general')
            tipo_habitacion = Tipo_Habitacion.objects.get(descripcion='simple')
            compra = Orden_Compra.objects.get(num_compra=int(id))

            Listado_Trabajador.objects.create(
                    rut=rut,
                    nombres=nombres,
                    apaterno=apaterno,
                    amaterno=amaterno,
                    celular=celular,
                    tipo_comedor= tipo_comedor,
                    tipo_habitacion = tipo_habitacion,
                    orden_compra= compra
                    )






    return render(request,'cliente/crear_trabajador.html',data)



def solicitarOrden(request):

    data = {
            'form':SolicitarOrdenForm()
            }

    if request.method == 'POST':
        formulario = SolicitarOrdenForm(data=request.POST)

        if formulario.is_valid():
            print('el formulario esta todo correcto')








    return render(request,'cliente/crear_orden.html',data)
