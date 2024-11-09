from __future__ import annotations

import csv
import io

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from django.template import loader

from .forms import ReporteForm
from .models import Reporte

UNSAFE_CACHE = None

def exportar(request: HttpRequest, cantidad: str = '*') -> HttpResponse:
    global UNSAFE_CACHE
    # Validar el parámetro cantidad
    cantidad = '*'
    if not cantidad.isdecimal() and cantidad != '*':
        raise Http404("Parámetro cantidad no es válido, se esperaba un número mayor a cero o en su defecto '*'")
    if cantidad != '*' and int(cantidad) < 1:
        raise Http404("Cantidad pedida inválida, se esperaba un número mayor a cero")
   
    if not UNSAFE_CACHE:
        datos = Reporte.objects.all()  # Obtener todos los registros
            
        # Crear un flujo de datos en memoria
        output = io.StringIO()
        
        # Crear el writer para escribir el CSV en el stream
        writer = csv.writer(output)
        writer.writerow(['cuenta', 'fecha', 'monto', 'descripcion'])  # Encabezados
        
        # Escribir los datos en el stream
        for dato in datos:
            writer.writerow([dato.cuenta, dato.fecha, dato.monto, dato.descripcion])
        
        # Guardar el stream en el caché (puedes usar el contenido de output.getvalue() donde necesites)
        UNSAFE_CACHE = output.getvalue()

    # Si el usuario pide todos los registros
    if cantidad == '*':
        threshold = 6000  
    else:
        threshold = int(cantidad)  
    
    # Leer el CSV del caché y cargar los datos al contexto
    input_stream = io.StringIO(UNSAFE_CACHE)
    reader = csv.reader(input_stream)
    
    # Omitir la primera fila (encabezados)
    next(reader)
    
    # Cargar los datos del CSV en la variable `datos`
    datos = [{'cuenta': row[0], 'fecha': row[1], 'monto': row[2], 'descripcion': row[3]} for row, _ in zip(reader, range(threshold))]
    
    # Traer el template
    template = loader.get_template('reporte_tabla.html')
    context = {
        'reportes': datos,  # Cargar los datos procesados
        'cantidad': cantidad,
    }

    return HttpResponse(template.render(context, request))


def exportar(request: HttpRequest) -> HttpResponse:
    reportes = Reporte.objects.all()
    return render(request, 'reporte_tabla.html', context={'reportes': reportes})


def crear_reporte(request: HttpRequest) -> HttpRequest:
    if request.method == 'POST':
        form = ReporteForm(request.POST)
        if form.is_valid():
            form.save()        
    else:
        form = ReporteForm()
    return render(request, 'crear-reportes.html', context={'form': form})
