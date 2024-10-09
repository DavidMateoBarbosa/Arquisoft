from django.urls import path
from . import views

urlpatterns = [
    path('exportar-csv/', views.exportar_datos_contables_csv, name='exportar_csv'),
]