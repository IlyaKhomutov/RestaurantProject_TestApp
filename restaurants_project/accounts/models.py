import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.username}"
