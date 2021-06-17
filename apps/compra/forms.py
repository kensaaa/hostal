from django import forms
from .models import Orden_Compra,Huesped,Gasto_Huesped_Plato



class OrdenCompraForm(forms.ModelForm):

    class Meta:
        model = Orden_Compra
        fields ='__all__'




class HuespedForm(forms.ModelForm):

    class Meta:
        model = Huesped
        fields ='__all__'




class GastoForm(forms.ModelForm):

    class Meta:
        model = Gasto_Huesped_Plato
        fields ='__all__'
