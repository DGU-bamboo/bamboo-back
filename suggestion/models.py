from django.db import models
from core.models import Base


class Suggestion(Base):
    content = models.TextField()
    image = models.ImageField(upload_to="suggestion/", blank=True, null=True)
    contact = models.EmailField(blank=True, null=True)
