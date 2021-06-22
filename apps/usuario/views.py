from django.shortcuts import render,redirect
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy
from .forms import *
from .models import *


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('home')
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')




def RegristrarCLiente(request):

    data = {
            'form':FormularioCliente()
            }
    
    if request.method == 'POST':
        formulario = FormularioCliente(data=request.POST)

        if formulario.is_valid():

            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            rut = formulario.cleaned_data['rut']
            nombre = formulario.cleaned_data['nombre']
            celular = formulario.cleaned_data['celular']
            correo = formulario.cleaned_data['correo']

            usuario = User.objects.create_user(username=username,password=password)
            id_usuario = usuario.id
            Cliente.objects.create(rut=rut,nombre=nombre,celular=celular,correo=correo,usuario=id_usuario)
            login(request,usuario)

            return redirect(to='home')

        data['form'] = formulario



    return render(request,'usuario/cliente/registrarCliente.html',data)








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
