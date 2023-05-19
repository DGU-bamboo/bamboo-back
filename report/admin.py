from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from report.filters import NemoApproveFilter, CommonApproveFilter, ReportFilter
from report.models import (
    Question,
    Report,
    MaintainerNemoReport,
    MaintainerCommonReport,
    MaintainerQuestion,
)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_filter = [ReportFilter]
    list_display = [
        "id",
        "type",
        "short_content",
        "created_at",
        "is_student",
        "is_approved",
    ]

    def short_content(self, instance):
        return instance.content[:20]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "content", "answer"]


@admin.register(MaintainerNemoReport)
class MaintainerNemoReportAdmin(admin.ModelAdmin):
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
    list_display = ["id", "short_content", "created_at", "is_student", "is_approved"]

    def short_content(self, instance):
        return instance.content[:20]

    def get_queryset(self, request):
        return (
            super().get_queryset(request).filter(type="NEMO", deleted_at__isnull=True)
        )


@admin.register(MaintainerCommonReport)
class MaintainerCommonReportAdmin(admin.ModelAdmin):
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
class MaintainerQuestionAdmin(admin.ModelAdmin):
    exclude = [
        "deleted_at",
    ]
    list_display = ["id", "content", "answer"]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).filter(deleted_at__isnull=True)
