from django.db import models
from django.contrib.auth import get_user_model

from .validators import validate_year

User = get_user_model()

class Book(models.Model):
    title = models.CharField(
        verbose_name='Название книги',
        max_length=100
    )
    author = models.CharField(
        verbose_name='Автор книги',
        max_length=100
    )
    publication_year = models.PositiveSmallIntegerField(
        verbose_name='Год издания',
        validators=[validate_year]
    )
    isbn = models.CharField(
        verbose_name='ISBN',
        max_length=13
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title
