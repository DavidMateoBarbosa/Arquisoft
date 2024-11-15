from django.http import HttpRequest, HttpResponse

from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm
from django.core import serializers
from django.contrib.auth.decorators import login_required
from whiletrue.auth0backend import getRole



# Create your views here.
@login_required
def usuarios_obtener(request: HttpRequest) -> HttpResponse:
    role= getRole(request)
    if role in ["Administrador", "Usuario"]:
        users = Usuario.objects.all()
        return render(request, 'usuarios_template.html', context={'usuarios': users, 'cantidad': len(users)})  # missing front
    else:
        return HttpResponse("Usuario No Autorizado")
    

@login_required
def usuarios_crear(request: HttpRequest) -> HttpResponse:
    role= getRole(request)
    if role =="Administrador": 
        if request.method == 'POST':
            form = UsuarioForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = UsuarioForm()  
        return render(request, 'crearUsuarios_template.html', context={'form': form}) 
    else:
        return HttpResponse("Usuario No Autorizado")
