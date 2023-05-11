from django.db import models
from core.models import BaseModel
from post.models import Post


class AbstractReport(BaseModel):
    content = models.TextField()
    password = models.CharField(max_length=15)
    is_student = models.BooleanField(default=False)
    is_approve = models.BooleanField(null=True)
    approved_at = models.DateTimeField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    filtered_content = models.TextField()

    class Meta:
        abstract = True


class NemoReport(AbstractReport):
    pass


class CommonReport(AbstractReport):
    image = models.ImageField(null=True, blank=True)


class CommentReport(AbstractReport):
    post_num = models.PositiveIntegerField()


class Question(BaseModel):
    content = models.TextField()
    answer = models.TextField()
