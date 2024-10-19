import hashlib

from django.contrib.auth.hashers import make_password
from django.db import models

class Usuario(models.Model): 
    username: str = models.CharField(max_length=255)
    password: str = models.CharField(max_length=255)
    email: str = models.EmailField()
    firstname: str = models.CharField(max_length=50)
    lastname: str = models.CharField(max_length=50)

    def save(self, *args, **kwargs) -> None:
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(hashlib.sha512(self.password.encode()).hexdigest())
        super().save(*args, **kwargs)
