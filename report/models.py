from core.models import BaseModel
from django.db import models
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
    is_approved = models.BooleanField(null=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    filtered_content = models.TextField(default="")

    @property
    def postify(self):
        if not self.deleted_at:
            content = (
                self.created_at.strftime("%Y.%m.%d %p %I:%M:%S")
                + (" 🐘" if self.is_student else "")
                + f"\n{self.filtered_content}"
            )
        else:
            content = (
                self.created_at.strftime("%Y.%m.%d %p %I:%M:%S")
                + (" 🐘" if self.is_student else "")
                + f"\n< 작성자의 요청에 의해 삭제된 제보입니다. >"
            )
        return content


class MaintainerNemoReport(Report):
    class Meta:
        proxy = True
        verbose_name = "니모 제보 (관리자용)"
        verbose_name_plural = "니모 제보들 (관리자용)"


class MaintainerCommonReport(Report):
    class Meta:
        proxy = True
        verbose_name = "일반 제보 (관리자용)"
        verbose_name_plural = "일반 제보들 (관리자용)"


class Question(BaseModel):
    content = models.CharField(max_length=100)
    answer = models.CharField(max_length=20)


class MaintainerQuestion(Question):
    class Meta:
        proxy = True
        verbose_name = "재학생 인증 질문 (관리자용)"
        verbose_name_plural = "재학생 인증 질문들 (관리자용)"
