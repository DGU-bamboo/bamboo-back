from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from core.utils.discord import send_to_discord
from django.conf import settings
from post.models import Post


@receiver(post_save, sender=Post)
def suggestion_discord_sender(sender, instance, created, **kwargs):
    if created:
        # todo: admin 추가하고 관리자용 어드민으로 변경
        url = settings.DISCORD_WEBHOOK_URL_UPLOAD
        if instance.type == "NEMO":
            admin_link = f"{settings.WEB_URL}/admin/post/post/{instance.id}/change/"
            message = f"""[니모제보 글 업로드 완료]({admin_link})
                        """
            send_to_discord(url, message)
        elif instance.type == "COMMON":
            admin_link = f"{settings.WEB_URL}/admin/post/post/{instance.id}/change/"
            message = f"""[일반제보 글 업로드 완료]({admin_link})"""
            send_to_discord(url, message)
