from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import *


class FormularioLogin(AuthenticationForm):

    def __init__(self,*args,**kwargs):
        super(FormularioLogin,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contrasena'



class FormularioCliente(forms.Form):
    username = forms.CharField(label='Usuario',required=True)
    rut = forms.CharField(label='Rut Empresa',required=True)
    nombre = forms.CharField(label='Nombre Empresa',required=True)
    celular = forms.IntegerField(label='Celular',required=True)
    correo = forms.EmailField(label='Correo',required=True)
    password1 = forms.CharField(label='Contrasena',required=True)
    password2 = forms.CharField(label='Confirmacion Contrasena',required=True)












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
