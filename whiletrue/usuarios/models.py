from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser): 
    def __str__(self) -> str:
        return f'User(username={self.username}, isadmin={self.is_staff}, active={self.is_active})'
