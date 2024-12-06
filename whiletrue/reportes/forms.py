from django import forms
from .models import Reporte


class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = [
            'cuenta',
            'fecha',
            'monto',
            'monto2',
            'monto3',
            'montototal',
            'descripcion'
        ]
        labels = {
            'cuenta': 'Cuenta',
            'fecha': 'Fecha',
            'monto': 'Monto1',
            'monto2': 'Monto2',
            'monto3': 'Monto3',
            'montototal': 'montototal',
            'descripcion': 'Descripcion'
        }

