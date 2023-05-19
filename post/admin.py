from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from post.filters import PostTypeFilter, CommentApproveFilter
from post.models import Post, Comment, MaintainerComment, MaintainerPost
from report.models import MaintainerCommonReport, MaintainerNemoReport


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = [PostTypeFilter]
    list_display = ["id", "type", "title"]
    search_fields = ["id", "content", "title"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = [CommentApproveFilter]
    list_display = ["id", "post_num", "short_content", "created_at", "is_approved"]
    search_fields = ["filtered_content"]

    def short_content(self, instance):
        return instance.content[:30]


class MaintainerNemoReportInline(admin.TabularInline):
    model = MaintainerNemoReport
    show_change_link = True
    can_delete = False
    fields = ["id", "content"]
    readonly_fields = ["content"]
    extra = 0

    def has_add_permission(self, request: HttpRequest, instance) -> bool:
        return False

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return (
            super().get_queryset(request).filter(type="NEMO", deleted_at__isnull=True)
        )


class MaintainerCommonReportInline(admin.TabularInline):
    model = MaintainerCommonReport
    show_change_link = True
    can_delete = False
    fields = ["id", "content"]
    readonly_fields = ["content"]
    extra = 0

    def has_add_permission(self, request: HttpRequest, instance) -> bool:
        return False

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return (
            super().get_queryset(request).filter(type="COMMON", deleted_at__isnull=True)
        )


class MaintainerCommentInline(admin.TabularInline):
    model = MaintainerComment
    show_change_link = True
    can_delete = False

    fields = ["id", "filtered_content"]
    readonly_fields = ["filtered_content"]
    extra = 0

    def has_add_permission(self, request: HttpRequest, instance) -> bool:
        return False

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).filter(deleted_at__isnull=True)


@admin.register(MaintainerPost)
class MaintainerPostAdmin(admin.ModelAdmin):
    readonly_fields = [
        "title",
        "type",
        "content",
        "is_student",
        "created_at",
    ]
    exclude = [
        "deleted_at",
    ]
    list_filter = [PostTypeFilter]
    list_display = ["id", "type", "title"]
    inlines = [
        MaintainerNemoReportInline,
        MaintainerCommonReportInline,
        MaintainerCommentInline,
    ]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).filter(deleted_at__isnull=True)


@admin.register(MaintainerComment)
class MaintainerCommentAdmin(admin.ModelAdmin):
    readonly_fields = [
        "post_num",
        "content",
        "password",
        "is_student",
        "approved_at",
        "post",
    ]
    search_fields = ["filtered_content"]
    exclude = [
        "deleted_at",
    ]
    list_filter = [CommentApproveFilter]
    list_display = ["id", "post_num", "short_content", "created_at", "is_approved"]

    def short_content(self, instance):
        return instance.content[:30]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).filter(deleted_at__isnull=True)
