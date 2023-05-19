from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from report.filters import NemoApproveFilter, CommonApproveFilter
from report.models import (
    Question,
    Report,
    MaintainerNemoReport,
    MaintainerCommonReport,
    MaintainerQuestion,
)

admin.site.register(Report)
admin.site.register(Question)


@admin.register(MaintainerNemoReport)
class NemoReportAdmin(admin.ModelAdmin):
    readonly_fields = [
        "content",
        "password",
        "type",
        "is_student",
        "post",
    ]
    exclude = [
        "deleted_at",
    ]
    list_filter = [NemoApproveFilter]
    list_display = ["id", "is_student", "created_at", "is_approved"]

    def get_queryset(self, request):
        return (
            super().get_queryset(request).filter(type="NEMO", deleted_at__isnull=True)
        )


@admin.register(MaintainerCommonReport)
class CommonReportAdmin(admin.ModelAdmin):
    readonly_fields = [
        "content",
        "password",
        "type",
        "is_student",
        "post",
    ]
    exclude = [
        "deleted_at",
    ]
    list_filter = [CommonApproveFilter]
    list_display = ["id", "is_student", "created_at", "is_approved"]

    def get_queryset(self, request):
        return (
            super().get_queryset(request).filter(type="COMMON", deleted_at__isnull=True)
        )


@admin.register(MaintainerQuestion)
class QuestionAdmin(admin.ModelAdmin):
    exclude = [
        "deleted_at",
    ]
    list_display = ["id", "content", "answer"]
