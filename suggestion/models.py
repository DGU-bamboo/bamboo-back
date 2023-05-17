from django.db import models
from core.models import BaseModel


class Suggestion(BaseModel):
    content = models.TextField(default="")
    contact = models.EmailField(blank=True, null=True)
    memo = models.TextField(blank=True, default="")
