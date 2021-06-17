from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from .forms import *
from .models import *



class ListarCliente(ListView):
    model = Cliente
    template_name = 'usuario/cliente/listar_cliente.html'
    context_object_name = 'clientes'
    queryset = Cliente.objects.all()




class ListarProveedor(ListView):
    model = Proveedor
    template_name = 'usuario/proveedor/listar_proveedor.html'
    context_object_name = 'provedores'
    queryset = Proveedor.objects.all()




class ListarEmpleado(ListView):
    model = Empleado
    template_name = 'usuario/empleado/listar_empleado.html'
    context_object_name = 'empleados'
    queryset = Empleado.objects.all()







class CrearProveedor(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'usuario/proveedor/crear_proveedor.html'
    success_url = reverse_lazy('usuario:listar_proveedor')




class CrearCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'usuario/cliente/crear_cliente.html'
    success_url = reverse_lazy('usuario:listar_cliente')




class CrearEmpleado(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'usuario/empleado/crear_empleado.html'
    success_url = reverse_lazy('usuario:listar_empleado')








class ActualizarCliente(UpdateView):
    model = Cliente
    template_name = 'usuario/cliente/actualizar_cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('usuario:listar_cliente')




class ActualizarProveedor(UpdateView):
    model = Proveedor
    template_name = 'usuario/proveedor/actualizar_proveedor.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('usuario:listar_proveedor')




class ActualizarEmpleado(UpdateView):
    model = Empleado
    template_name = 'usuario/empleado/actualizar_empleado.html'
    form_class = EmpleadoForm
    success_url = reverse_lazy('usuario:listar_empleado')
