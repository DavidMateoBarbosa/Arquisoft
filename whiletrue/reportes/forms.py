from django import forms
from .models import Reporte


class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = [
            'cuenta',
            'fecha',
            'monto',
            'descripcion'
        ]
        labels = {
            'cuenta': 'Cuenta',
            'fecha': 'Fecha',
            'monto': 'Monto',
            'descripcion': 'Descripcion'
        }

