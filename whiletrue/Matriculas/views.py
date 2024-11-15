from django.http import HttpRequest, HttpResponse

from django.shortcuts import render, redirect
from .models import Matriculado
from django.core import serializers
from .forms import MatriculadoForm
from django.contrib.auth.decorators import login_required
from whiletrue.auth0backend import getRole



@login_required
def matriculadosObtener(request: HttpRequest) -> HttpResponse:
    role = getRole(request)
    if role in ["Administrador", "Usuario"]:
        estudiantes = Matriculado.objects.all()
        for estudiante in estudiantes:
            estudiante.decrypt_fields()
        return render(request, 'estudiantes_template.html', context={'Estudiantes': estudiantes}) 
    else:
        return HttpResponse("Usuario No Autorizado") 

        
    
@login_required
def matriculadosCrear(request: HttpRequest) -> HttpResponse:
    role = getRole(request)
    if role == "Administrador":
        if request.method == 'POST':
            form = MatriculadoForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = MatriculadoForm()
        return render(request, 'crearMatriculados_template.html', context={'form': form}) 
    else:
        return HttpResponse("Usuario No Autorizado") 

