from django import forms
from .models import Plato


class PlatoForm(forms.ModelForm):

    class Meta:
        model = Plato
        fields = '__all__'
