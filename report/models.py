from django.db import models
from core.models import BaseModel
from post.models import Post


class AbstractReport(BaseModel):
    content = models.TextField(default="")
    password = models.PositiveSmallIntegerField()
    is_student = models.BooleanField(default=False)
    is_approved = models.BooleanField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    filtered_content = models.TextField(default="")

    class Meta:
        abstract = True


class NemoReport(AbstractReport):
    pass


class CommonReport(AbstractReport):
    pass


class CommentReport(AbstractReport):
    post_num = models.PositiveIntegerField()
    approved_at = models.DateTimeField(null=True, blank=True)


class Question(BaseModel):
    content = models.CharField(max_length=100)
    answer = models.CharField(max_length=20)
