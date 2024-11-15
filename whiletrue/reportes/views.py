from __future__ import annotations

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from django.template import loader
from django.contrib.auth.decorators import login_required
from whiletrue.auth0backend import getRole
from .forms import ReporteForm
from .models import Reporte


@login_required
def exportar(request: HttpRequest) -> HttpResponse:
    if getRole(request) not in ("Administrador", "Usuario"):
        return HttpResponse("Usuario No Autorizado") 
    reportes = Reporte.objects.all()
    return render(request, 'reporte_tabla.html', context={'reportes': reportes})


@login_required
def crear_reporte(request: HttpRequest) -> HttpRequest:
    if request.method == 'POST':
        if getRole(request) != 'Administrador':
            return HttpResponse("Usuario No Autorizado") 
        form = ReporteForm(request.POST)
        if form.is_valid():
            form.save()        
    else:
        form = ReporteForm()
    return render(request, 'crear-reportes.html', context={'form': form})
