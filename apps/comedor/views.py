from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from .models import Plato
from .forms import PlatoForm


class ListarPlato(ListView):
    model = Plato
    template_name = 'comedor/listar_plato.html'
    context_object_name = 'platos'
    queryset = Plato.objects.all()




class CrearPlato(CreateView):
    model = Plato
    form_class = PlatoForm
    template_name = 'comedor/crear_plato.html'
    success_url = reverse_lazy('comedor:listar_plato')




class ActualizarPlato(UpdateView):
    model = Plato
    form_class = PlatoForm
    template_name = 'comedor/actualizar_plato.html'
    success_url = reverse_lazy('comedor:listar_plato')
