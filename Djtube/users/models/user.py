from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phonenumber = models.CharField(
        max_length=16,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.phonenumber
