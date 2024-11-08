from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('fetch/', views.exportar),
    path('crear/', csrf_exempt(views.crear_reporte), name='crear')
]
