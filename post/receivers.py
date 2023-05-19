from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from core.utils.discord import send_to_discord
from django.conf import settings
from post.models import Post, Comment, MaintainerComment, MaintainerPost
from django.utils import timezone
from post.signals import send_discord_upload


@receiver(send_discord_upload)
def post_discord_sender(post, **kwargs):
    url = settings.DISCORD_WEBHOOK_URL_UPLOAD
    if post.type == "NEMO":
        admin_link = f"{settings.WEB_URL}/admin/post/maintainerpost/{post.id}/change/"
        message = f"""[니모제보 글 업로드 완료]({admin_link})
                    """
        send_to_discord(url, message)
    elif post.type == "COMMON":
        admin_link = f"{settings.WEB_URL}/admin/post/maintainerpost/{post.id}/change/"
        message = f"""[일반제보 글 업로드 완료]({admin_link})"""
        send_to_discord(url, message)


@receiver(post_save, sender=Post)
def add_id_hashtag_in_post(sender, instance, created, **kwargs):
    if created:
        hashtag = " #" + str(instance.id) + "번째뿌우"
        instance.content += hashtag
        instance.save(update_fields=["content"])
        send_discord_upload.send(sender="add id hashtag in post", post=instance)


@receiver(pre_save, sender=Comment)
@receiver(pre_save, sender=MaintainerComment)
def comment_pre_save(sender, instance, **kwargs):
    try:
        old_instance = Comment.objects.get(pk=instance.pk)
    except Comment.DoesNotExist:
        return
    if old_instance.is_approved != True and instance.is_approved == True:
        instance.approved_at = timezone.now()


@receiver(post_save, sender=Comment)
@receiver(post_save, sender=MaintainerComment)
def comment_post_save(sender, instance, created, **kwargs):
    if created:
        # todo: admin 추가하고 관리자용 어드민으로 변경
        reject_url = f"{settings.API_URL}/comments/{instance.id}/reject"
        comment_admin_link = (
            f"{settings.WEB_URL}/admin/post/maintainercomment/{instance.id}/change/"
        )
        post_admin_link = (
            f"{settings.WEB_URL}/admin/post/maintainerpost/{instance.post.id}/change/"
        )
        url = settings.DISCORD_WEBHOOK_URL_NEMO
        message = f"""[내 목소리가 들리나요? 댓글 달아주세요!]({comment_admin_link})
                        > 댓글 내용 : {instance.content}
                        > 재학생 여부 : {instance.is_student}
                        > [글 링크]({post_admin_link})
                        > [거절하기]({reject_url})"""
        send_to_discord(url, message)
