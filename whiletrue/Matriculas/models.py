from django.db import models
from cryptography.fernet import Fernet
from django.conf import settings
import hashlib

class Matriculado(models.Model):
    nombre = models.TextField(default="N/A")  # Cambiado de CharField a TextField
    documentoid = models.TextField()  # Cambiado de CharField a TextField
    hashDocumentoId = models.TextField(default="N/A")
    periodo_inscripcion = models.TextField(default="N/A")  # Cambiado de CharField a TextField
    direccion = models.TextField(default="N/A")  # Cambiado de CharField a TextField
    hashDireccion = models.TextField(default="N/A")
    email = models.TextField(default="N/A")  # Cambiado de CharField a TextField
    hashEmail = models.TextField(default="N/A")
    
    
    def save(self, *args, **kwargs):
        f = Fernet(settings.ENCRYPT_KEY)
        if self.documentoid:  # Asegúrate de que no sea nulo
            self.hashDocumentoId= hashlib.sha256(self.documentoid.encode("utf-8")).hexdigest()
            self.documentoid = f.encrypt(self.documentoid.encode("utf-8")).decode("utf-8")
        if self.direccion:
            self.hashDireccion= hashlib.sha256(self.direccion.encode("utf-8")).hexdigest()
            self.direccion = f.encrypt(self.direccion.encode("utf-8")).decode("utf-8")
        if self.email:
            self.hashEmail= hashlib.sha256(self.email.encode("utf-8")).hexdigest()
            self.email = f.encrypt(self.email.encode("utf-8")).decode("utf-8")
        super().save(*args, **kwargs)

    def decrypt_fields(self):
        f = Fernet(settings.ENCRYPT_KEY)
        if self.documentoid:
            self.documentoid = f.decrypt(self.documentoid.encode("utf-8")).decode("utf-8")
            #Calculamos el hash local
            hashLocalDocumentoId= hashlib.sha256(self.documentoid.encode("utf-8")).hexdigest()
            if hashLocalDocumentoId!=self.hashDocumentoId:
                print("Se cumple")
                self.documentoid="El dato fue alterado"           
        if self.direccion:
            self.direccion = f.decrypt(self.direccion.encode("utf-8")).decode("utf-8")
            hashLocalDireccion= hashlib.sha256(self.direccion.encode("utf-8")).hexdigest()
            if hashLocalDireccion!=self.hashDireccion:
                self.direccion="El dato fue alterado"
        if self.email:
            self.email = f.decrypt(self.email.encode("utf-8")).decode("utf-8")
            hashLocalEmail= hashlib.sha256(self.email.encode("utf-8")).hexdigest()
            if hashLocalEmail!=self.hashEmail:
                self.email="El dato fue alterado"