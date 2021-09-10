from django.db import models
from django.contrib.auth.models import AbstractUser
from .user_manager import UserManager


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return self.email
