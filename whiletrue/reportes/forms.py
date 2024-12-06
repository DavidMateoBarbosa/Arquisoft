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
            'descripcion'
        ]
        labels = {
            'cuenta': 'Cuenta',
            'fecha': 'Fecha',
            'monto': 'Monto1',
            'monto2': 'Monto2',
            'monto3': 'Monto3',
            'descripcion': 'Descripcion'
        }

