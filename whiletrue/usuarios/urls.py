from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.usuarios_obtener),
    path('usuariosCrear/', views.usuarios_crear),
]