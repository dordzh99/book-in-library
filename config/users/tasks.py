from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from config.settings import EMAIL_HOST_USER

User = get_user_model()

@shared_task
def send_message(user_id):
    user = User.objects.get(pk=user_id)
    send_mail(
        'Добро пожаловать!',
        'Вы успешно зарегистрированы на нашем сервере!',
        EMAIL_HOST_USER,
        [user.email]
    )
