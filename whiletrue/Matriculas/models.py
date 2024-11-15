from django.db import models
from cryptography.fernet import Fernet
from django.conf import settings

class Matriculado(models.Model):
    nombre = models.TextField(default="N/A")  # Cambiado de CharField a TextField
    documentoid = models.TextField()  # Cambiado de CharField a TextField
    periodo_inscripcion = models.TextField(default="N/A")  # Cambiado de CharField a TextField
    direccion = models.TextField(default="N/A")  # Cambiado de CharField a TextField
    email = models.TextField(default="N/A")  # Cambiado de CharField a TextField
    
    
    def save(self, *args, **kwargs):
        f = Fernet(settings.ENCRYPT_KEY)
        if self.documentoid:  # Asegúrate de que no sea nulo
            self.documentoid = f.encrypt(self.documentoid.encode("utf-8")).decode("utf-8")
        if self.direccion:
            self.direccion = f.encrypt(self.direccion.encode("utf-8")).decode("utf-8")
        if self.email:
            self.email = f.encrypt(self.email.encode("utf-8")).decode("utf-8")
        super().save(*args, **kwargs)

    def decrypt_fields(self):
        f = Fernet(settings.ENCRYPT_KEY)
        if self.documentoid:
            self.documentoid = f.decrypt(self.documentoid.encode("utf-8")).decode("utf-8")
        if self.direccion:
            self.direccion = f.decrypt(self.direccion.encode("utf-8")).decode("utf-8")
        if self.email:
            self.email = f.decrypt(self.email.encode("utf-8")).decode("utf-8")