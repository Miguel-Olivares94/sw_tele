# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SomeModel

@receiver(post_save, sender=SomeModel)
def my_handler(sender, instance, created, **kwargs):
    # Evitar consultas a la base de datos aquí
    pass
