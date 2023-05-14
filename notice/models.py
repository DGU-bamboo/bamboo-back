from django.db import models

from core.models import BaseModel


class Notice(BaseModel):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to="notice/", blank=True, null=True)
