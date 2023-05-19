from django.dispatch import receiver
from django.db.models.signals import post_save
from core.utils.discord import send_to_discord
from suggestion.models import Suggestion
from django.conf import settings


@receiver(post_save, sender=Suggestion)
def suggestion_discord_sender(sender, instance, created, **kwargs):
    if created:
        admin_link = f"{settings.WEB_URL}/admin/suggestion/maintainersuggestion/{instance.id}/change/"
        url = settings.DISCORD_WEBHOOK_URL_SUGGESTION
        message = f"""[건의사항이 도착했어요!]({admin_link})
                    > 건의 내용 : {instance.content}
                    > 연락처 : {instance.contact}"""
        send_to_discord(url, message)
