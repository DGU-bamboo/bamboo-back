from core.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(BaseModel):
    class PostType(models.TextChoices):
        COMMON = "COMMON", _("COMMON")
        NEMO = "NEMO", _("NEMO")

    type = models.CharField(choices=PostType.choices, max_length=15)
    content = models.TextField()
