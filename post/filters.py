from typing import Any, Optional
from django.contrib import admin
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _


class PostTypeFilter(admin.SimpleListFilter):
    title = _("게시글 타입 관련 필터")
    parameter_name = "post_type_filter"

    def lookups(self, request, model_admin):
        return (
            ("NEMO", _("니모 제보 게시글")),
            ("COMMON", _("일반 제보 게시글")),
        )

    def queryset(self, request: Any, queryset):
        if self.value() == "NEMO":
            return queryset.filter(type="NEMO")
        if self.value() == "COMMON":
            return queryset.filter(type="COMMON")


class CommentApproveFilter(admin.SimpleListFilter):
    title = _("댓글 승인 관련 필터")
    parameter_name = "comment_approve_filter"

    def lookups(self, request, model_admin):
        return (
            ("UPLOADED", _("업로드된 댓글")),
            ("NULL", _("승인 확인이 필요한 댓글")),
            ("REJECTED", _("반려된 댓글")),
        )

    def queryset(self, request: Any, queryset):
        if self.value() == "UPLOADED":
            return queryset.filter(post__isnull=False)
        if self.value() == "NULL":
            return queryset.filter(is_approved=None)
        if self.value() == "REJECTED":
            return queryset.filter(is_approved=False)
