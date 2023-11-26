from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Book(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=100
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name='Автор'
    )
    publication_year = models.DateField(
        auto_now_add=True,
        verbose_name='Год издания'
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
