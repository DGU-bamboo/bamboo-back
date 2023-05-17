from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _
from post.models import Post


class Report(BaseModel):
    class ReportType(models.TextChoices):
        COMMON = "COMMON", _("COMMON")
        NEMO = "NEMO", _("NEMO")

    type = models.CharField(choices=ReportType.choices, max_length=15)
    content = models.TextField(default="")
    is_student = models.BooleanField(default=False)
    password = models.CharField(max_length=4)
    is_approved = models.BooleanField(default=False, null=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    filtered_content = models.TextField()


class Question(BaseModel):
    content = models.CharField(max_length=100)
    answer = models.CharField(max_length=20)
