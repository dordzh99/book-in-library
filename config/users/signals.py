from django.dispatch import receiver
from djoser import signals

from .tasks import send_message

@receiver(signals.user_registered)
def send_welcome_message_handler(sender, request, user, **kwargs):
    send_message.delay(user.email)
