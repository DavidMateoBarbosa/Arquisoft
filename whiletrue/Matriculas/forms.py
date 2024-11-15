from django import forms
from .models import Matriculado


class MatriculadoForm(forms.ModelForm):
    class Meta:
        model = Matriculado
        fields = [
            'nombre',
            'documentoid',
            'periodo_inscripcion',
            'direccion',
            'email'
        ]
        labels = {
            'nombre': 'Nombre',
            'documentoid': 'Documentoid',
            'periodo_inscripcion': 'PeriodoInscripcion',
            'direccion': 'Direccion',
            'email': 'Email'
            
            
        }

