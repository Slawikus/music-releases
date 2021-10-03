from django.db import models
from django.contrib.auth.models import AbstractUser
from .user_manager import UserManager


class User(AbstractUser):
    name = models.CharField(
        "Name",
        max_length=255,
        help_text="Full name/alias/nickname as you would usually sign your emails, "
                  "e.g. John Johnson or Lord Demogorgon."
    )
    email = models.EmailField(
        unique=True,
        help_text="The email address of the main label. It will be needed for logging in."
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    username = None
    first_name = None
    last_name = None

    objects = UserManager()

    def __str__(self):
        return f"{self.name} ({self.email}"
