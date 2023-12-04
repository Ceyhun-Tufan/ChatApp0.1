from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Message

@receiver(pre_save, sender=Message)
def update_username(sender, instance, **kwargs):
    # Eğer user değeri atanmışsa username'i güncelle
    if instance.user:
        instance.username = instance.user.username
