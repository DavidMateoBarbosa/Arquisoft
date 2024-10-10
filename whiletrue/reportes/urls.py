from django.urls import path
from . import views

urlpatterns = [
    path('', views.exportar),
    path('<str:cantidad>/', views.exportar),
    path('health-check/', views.healthCheck),
]