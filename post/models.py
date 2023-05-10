from lib2to3.pytree import Base
from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(Base):
    class PostType(models.TextChoices):
        COMMON = "COMMON", _("COMMON")
        NEMO = "NEMO", _("NEMO")

    type = models.CharField(choices=PostType.choices)
    content = models.TextField()
