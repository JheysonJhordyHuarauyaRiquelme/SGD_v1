# dojos/forms.py
from django import forms
from .models import Dojo

class DojoForm(forms.ModelForm):
    class Meta:
        model = Dojo
        fields = ['nombre', 'descripcion', 'ubicacion']
