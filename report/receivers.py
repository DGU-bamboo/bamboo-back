from django.dispatch import receiver
from django.db.models.signals import post_save
from core.utils.discord import send_to_discord
from report.models import *
from django.conf import settings


@receiver(post_save, sender=CommonReport)
def commom_discord_sender(sender, instance, created, **kwargs):
    if created:
        admin_link = (
            f"{settings.WEB_URL}/admin/report/commonreport/{instance.id}/change/"
        )
        url = settings.DISCORD_WEBHOOK_URL_COMMON
        message = f"""[일반 제보가 도착했어요! 두근세근]({admin_link})
                    > 일반 제보 내용 : {instance.content}
                    > 재학생 여부 : {instance.is_student}"""
        send_to_discord(url, message)
