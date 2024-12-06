from django.http import HttpRequest, HttpResponse, JsonResponse
import requests

from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm
from ..cypher import decrypt
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

def usuarios_obtenerJson(request: HttpRequest) -> JsonResponse:
    # URL de la API externa
    external_url = 'http://127.0.0.1:8000/reportes-csv/fetchjson/'

    # Realizar la solicitud HTTP a la API externa
    try:
        response = requests.get(external_url)
        response.raise_for_status()  # Lanza una excepción si hay un error en la solicitud
        data = response.json()  # Decodificar el JSON
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'Error al obtener datos de la API externa: {str(e)}'}, status=500)

    # Asegurar que los datos tengan la estructura esperada
    data = data.get('reportes')
    if data is not None:
        data = decrypt(data)
    else:
        data = []
    montos = {item['username']: float(item.get('montototal', 0)) for item in data}
    print(montos)

    # Obtener todos los usuarios de la base de datos
    usuarios = Usuario.objects.all()

    # Combinar los datos: asignar montos a los usuarios
    usuarios_con_montos = [
        {
            'username': usuario.username,
            'email': usuario.email,
            'monto': montos.get(usuario.username, 0)  # Si el username no está, asigna 0
        }
        for usuario in usuarios
    ]

    # Devolver los datos en formato JSON
    return JsonResponse({'usuarios': usuarios_con_montos})
