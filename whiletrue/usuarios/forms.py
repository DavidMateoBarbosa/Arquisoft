from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'password',
            'firstname',
            'lastname',
            'email',
        ]

        labels = {
            'username': 'Username',
            'password': 'Password',
            'firstname':'Firstname',
            'lastname':'Lastname',
            'email':'Email',
        }
