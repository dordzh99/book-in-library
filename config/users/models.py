from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    email = models.EmailField(
        verbose_name='Почта',
        unique=True
    )
    registration_date = models.DateField(default=timezone.now)
