from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=300, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    last_login = None
    first_name = None
    last_name = None
    is_superuser = None
    is_staff = None
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
