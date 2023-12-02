from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime as dt


class CustomUser(AbstractUser):
    """Кастомная модель пользователя."""

    email = models.EmailField(
        verbose_name='Почта',
        unique=True
    )
    registration_date = models.DateField(default=dt.date.today)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
