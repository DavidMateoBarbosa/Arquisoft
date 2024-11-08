from django.urls import path
from . import views

urlpatterns = [
    path('', views.exportar),
    path('crear/', views.crear_reporte)
]
