from django.http import HttpRequest, HttpResponse

from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm
from django.core import serializers


# Create your views here.
def usuarios_obtener(request: HttpRequest) -> HttpResponse:  # da todos y jsonifica
    return render(request, 'usuarios_template.html', context={'usuarios': serializers.serialize('json', Usuario.objects.all())})  # missing front
    
def usuarios_crear(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios/')  # Redirect after successful form submission
    else:
        form = UsuarioForm()  # If it's a GET request, create an empty form

    return render(request, 'crearxd.html', context={'form': form}) 
