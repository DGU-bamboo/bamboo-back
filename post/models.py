from core.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime


class Post(BaseModel):
    class PostType(models.TextChoices):
        COMMON = "COMMON", _("COMMON")
        NEMO = "NEMO", _("NEMO")
        ADMIN = "ADMIN", _("ADMIN")

    type = models.CharField(choices=PostType.choices, max_length=15)
    content = models.TextField(default="")
    is_student = models.BooleanField(default=False)


class Comment(BaseModel):
    post_num = models.CharField(max_length=15)
    approved_at = models.DateTimeField(null=True, blank=True)
    content = models.TextField(default="")
    password = models.CharField(max_length=4)
    is_student = models.BooleanField(default=False)
    is_approved = models.BooleanField(null=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    filtered_content = models.TextField(default="")
