from django.db import models
from django.contrib.auth.models import AbstractUser


# Override de Usuario
class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
