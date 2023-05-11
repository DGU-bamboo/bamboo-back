from django.dispatch import receiver
from django.db.models.signals import post_save
from core.utils.discord import send_to_discord
from suggestion.models import Suggestion
import requests


@receiver(post_save, sender=Suggestion)
def suggestion_discord_sender(sender, instance, created, **kwargs):
    if created:
        content = instance.content
        contact = instance.contact
        image = instance.image if instance.image else None
        send_to_discord(content, contact, image)
    else:
        pass
