from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('usuarios/', views.usuarios_obtener),
    path('usuariosJson/', views.usuarios_obtenerJson),
    path('usuariosCrear/', csrf_exempt(views.usuarios_crear), name='usuariosCrear'),
]