from django.http import HttpRequest, HttpResponse

from django.shortcuts import render, redirect
from .models import Matriculado
from django.core import serializers
from .forms import MatriculadoForm


# Create your views here.
def matriculadosObtener(request: HttpRequest) -> HttpResponse:
    estudiantes = Matriculado.objects.all()
    for estudiante in estudiantes:
        estudiante.decrypt_fields()
    return render(request, 'estudiantes_template.html', context={'Estudiantes': estudiantes})  
    

def matriculadosCrear(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = MatriculadoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MatriculadoForm()

    return render(request, 'crearMatriculados_template.html', context={'form': form}) 

