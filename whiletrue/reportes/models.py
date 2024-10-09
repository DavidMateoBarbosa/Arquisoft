from django.db import models

class Reporte(models.Model): 
    cuenta = models.CharField(max_length=100)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.cuenta} - {self.monto}"
    