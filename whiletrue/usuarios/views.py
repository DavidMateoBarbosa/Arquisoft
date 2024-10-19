from django.http import HttpRequest, HttpResponse

from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm
from django.core import serializers


# Create your views here.
def usuarios_obtener(request: HttpRequest) -> HttpResponse:
    users = Usuario.objects.all()
    return render(request, 'usuarios_template.html', context={'usuarios': users, 'cantidad': len(users)})  # missing front
    
def usuarios_crear(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm()

    return render(request, 'crearUsuarios_template.html', context={'form': form}) 
