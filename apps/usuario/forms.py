from django import forms
from .models import *


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'




class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = '__all__'




class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = '__all__'
