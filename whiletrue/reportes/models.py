from django.db import models

class Reporte(models.Model): 
    usuario = models.CharField(max_length=100)
    cuenta = models.CharField(max_length=100)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    monto2 = models.DecimalField(max_digits=10, decimal_places=2)
    monto3 = models.DecimalField(max_digits=10, decimal_places=2)
    montototal = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    
    def save(self, *args, **kwargs):
        # Calcular el monto total antes de guardar
        self.montototal = (self.monto or 0) + (self.monto2 or 0) + (self.monto3 or 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cuenta} - {self.monto}"
    