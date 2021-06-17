from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from .models import Habitacion
from .forms import HabitacionForm



class CrearHabitacion(CreateView):
    model = Habitacion
    form_class = HabitacionForm
    template_name = 'habitacion/crear_habitacion.html'
    success_url = reverse_lazy('habitacion:listar_habitacion')




class ListadoHabitacion(ListView):
    model = Habitacion
    template_name = 'habitacion/listar_habitacion.html'
    context_object_name = 'habitaciones'
    queryset = Habitacion.objects.all()




class ActualizarHabitacion(UpdateView):
    model = Habitacion
    template_name = 'habitacion/actualizar_habitacion.html'
    form_class = HabitacionForm
    success_url = reverse_lazy('habitacion:listar_habitacion')
