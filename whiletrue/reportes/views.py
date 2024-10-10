from __future__ import annotations

import csv

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from django.template import loader

from .models import Reporte

def exportar(request: HttpRequest, cantidad: str = '*') -> HttpResponse:
    # Validar el parámetro cantidad
    if not cantidad.isdecimal() and cantidad != '*':
        raise Http404("Parámetro cantidad no es válido, se esperaba un número mayor a cero o en su defecto '*'")
    if cantidad != '*' and int(cantidad) < 1:
        raise Http404("Cantidad pedida inválida, se esperaba un número mayor a cero")

    # Si el usuario pide todos los registros
    if cantidad == '*':
        datos = Reporte.objects.all()  # Obtener todos los registros
    else:
        # Si se especifica un número, limitar la cantidad de registros a devolver
        datos = Reporte.objects.all()[:int(cantidad)]

    #Traer el template
    template= loader.get_template('reporte_tabla.html')
    context = {
        'reportes': datos,
        'cantidad': cantidad,
    }
    
    render(request, 'reporte_tabla.html', context=context)
    return HttpResponse(template.render(context, request))


def healthCheck(request):
    return HttpResponse('ok')
