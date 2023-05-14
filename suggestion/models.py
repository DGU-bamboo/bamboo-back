from django.db import models
from core.models import BaseModel


class Suggestion(BaseModel):
    content = models.TextField()
    image = models.ImageField(upload_to="suggestion/", blank=True, null=True)
    contact = models.EmailField(blank=True, null=True)
    memo = models.TextField()
