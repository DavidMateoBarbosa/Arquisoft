from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'user',
            'password',
            'name',
            'lastname',
            'email'
        ]

        labels = {
            'user': 'User',
            'password': 'Password',
            'name':'Name',
            'lastname':'Lastname',
            'email':'Email'
        }
