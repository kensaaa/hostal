from django import forms
from .models import *


class DetalleForm(forms.ModelForm):

    class Meta:
        model = Detalle_Pedido
        fields = '__all__'




class OrdenPedidoForm(forms.ModelForm):

    class Meta:
        model = Orden_Pedido
        fields = '__all__'




class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'
