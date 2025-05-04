# examenes/forms.py
from django import forms
from .models import Examen, AlumnoExamen
# examenes/forms.py (continúa en el mismo archivo)
from alumnos.models import Alumno

class ExamenForm(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = Examen
        fields = ['titulo', 'descripcion', 'fecha', 'pago']



class AlumnoExamenForm(forms.ModelForm):
    class Meta:
        model = AlumnoExamen
        fields = ['alumno', 'examen']



class EvaluarExamenForm(forms.ModelForm):
    class Meta:
        model = AlumnoExamen
        fields = ['nota', 'aprobado']
