from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('matriculadosTotales/', views.matriculadosObtener),
    path('matriculaCrear/', csrf_exempt(views.matriculadosCrear), name='matriculadosCrear')
]