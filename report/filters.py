from typing import Any, Optional
from django.contrib import admin
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _


class NemoApproveFilter(admin.SimpleListFilter):
    title = _("니모 제보 승인 관련 필터")
    parameter_name = "nemo_approve_filter"

    def lookups(self, request, model_admin):
        return (
            ("UPLOADED", _("업로드된 니모")),
            ("NULL", _("승인 확인이 필요한 니모")),
            ("APPROVED", _("승인됐지만 게시되지 않은 니모")),
            ("REJECTED", _("반려된 니모")),
        )

    def queryset(self, request: Any, queryset):
        if self.value() == "UPLOADED":
            return queryset.filter(post__isnull=False)
        if self.value() == "NULL":
            return queryset.filter(is_approved=None)
        if self.value() == "APPROVED":
            return queryset.filter(post__isnull=True, is_approved=True)
        if self.value() == "REJECTED":
            return queryset.filter(is_approved=False)


class CommonApproveFilter(admin.SimpleListFilter):
    title = _("일반 제보 승인 관련 필터")
    parameter_name = "common_approve_filter"

    def lookups(self, request, model_admin):
        return (
            ("UPLOADED", _("업로드된 일반제보")),
            ("NULL", _("승인 확인이 필요한 일반제보")),
            ("REJECTED", _("반려된 일반제보")),
        )

    def queryset(self, request: Any, queryset):
        if self.value() == "UPLOADED":
            return queryset.filter(post__isnull=False)
        if self.value() == "NULL":
            return queryset.filter(is_approved=None)
        if self.value() == "REJECTED":
            return queryset.filter(is_approved=False)
