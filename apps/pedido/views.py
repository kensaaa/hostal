from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from .models import  Orden_Pedido,Detalle_Pedido,Producto
from .forms import OrdenPedidoForm,DetalleForm,ProductoForm






class CrearOrdenPedido(CreateView):
    model = Orden_Pedido
    form_class = OrdenPedidoForm
    template_name = 'pedido/ordenPedido/crear_pedido.html'
    success_url = reverse_lazy('pedido:listar_pedido')




class CrearDetallePedido(CreateView):
    model = Detalle_Pedido
    form_class = DetalleForm
    template_name = 'pedido/detalle/crear_detalle.html'
    success_url = reverse_lazy('pedido:listar_detalle')




class CrearProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'pedido/producto/crear_producto.html'
    success_url = reverse_lazy('pedido:listar_producto')







class ActualizarOrdenPedido(UpdateView):
    model = Orden_Pedido
    form_class = OrdenPedidoForm
    template_name = 'pedido/ordenPedido/actualizar_pedido.html'
    success_url = reverse_lazy('pedido:listar_pedido')




class ActualizarDetallePedido(UpdateView):
    model = Detalle_Pedido
    form_class = DetalleForm
    template_name = 'pedido/detalle/actualizar_detalle.html'
    success_url = reverse_lazy('pedido:listar_detalle')




class ActualizarProducto(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'pedido/producto/actualizar_producto.html'
    success_url = reverse_lazy('pedido:listar_producto')








class ListarOrdenPedido(ListView):
    model = Orden_Pedido
    template_name = 'pedido/ordenPedido/listar_pedido.html'
    context_object_name = 'pedidos'
    queryset = Orden_Pedido.objects.all()




class ListarDetallePedido(ListView):
    model = Detalle_Pedido
    template_name = 'pedido/detalle/listar_detalle.html'
    context_object_name = 'detalles'
    queryset = Detalle_Pedido.objects.all()




class ListarProducto(ListView):
    model = Producto
    template_name = 'pedido/producto/listar_producto.html'
    context_object_name = 'productos'
    queryset = Producto.objects.all()
