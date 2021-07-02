from django import forms
from datetime import date
from django.forms import ValidationError
from .models import Listado_Trabajador
from apps.comedor.models import Tipo_Comedor
from apps.habitacion.models import Tipo_Habitacion

class SolicitarOrdenForm(forms.Form):
    fecha_inicio = forms.DateField(label='fecha inicio servicio',required=True,input_formats=['%Y-%m-%d'],widget=forms.SelectDateWidget(),initial=date.today())
    fecha_termino = forms.DateField(label='fecha termino servicio',required=True,input_formats=['%Y-%m-%d'],widget=forms.SelectDateWidget(),initial=date.today())
    cantidad = forms.IntegerField(label='Cantidad Huespedes',required=True)

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']


        if cantidad > 4:
            raise ValidationError('la cantidad no debe superar el numero 4')


#   def clean_fecha_inicio(self):
#       fecha_inicio = self.cleaned_data['fecha_inicio']
#       fecha_actual = date.today()

#       if fecha_actual > fecha_inicio:
#           raise ValidationError('la fecha ingresada tiene que ser mayor a la actual')


#   def clean_fecha_termino(self):
#       fecha_termino = self.cleaned_data['fecha_termino']
#       fecha_inicio = self.cleaned_data['fecha_inicio']

#       if fecha_inicio > fecha_termino:
#           raise ValidationError('la fecha de termino debe ser mayor a la de inicio')

class TrabajadorForm(forms.Form):
    rut = forms.CharField(label='Rut',max_length=12,min_length=9)
    nombres = forms.CharField(label='Nombres',max_length=100,min_length=3)
    apaterno = forms.CharField(label='Apellido Paterno',max_length=100,min_length=3)
    amaterno = forms.CharField(label='Apellido Materno',max_length=100,min_length=3)
    celular = forms.IntegerField(label='Celular')
    comedor = forms.ModelChoiceField(queryset=Tipo_Comedor.objects.all())
    tipo_habitacion = forms.ModelChoiceField(queryset=Tipo_Habitacion.objects.all())
