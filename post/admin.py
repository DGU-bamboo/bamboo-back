from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from post.filters import PostTypeFilter, CommentApproveFilter
from post.models import Post, Comment, MaintainerComment, MaintainerPost

admin.site.register(Post)
admin.site.register(Comment)


@admin.register(MaintainerPost)
class PostAdmin(admin.ModelAdmin):
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

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).filter(deleted_at__isnull=True)


@admin.register(MaintainerComment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = [
        "post_num",
        "content",
        "password",
        "is_student",
        "approved_at",
    ]
    exclude = [
        "deleted_at",
    ]
    list_filter = [CommentApproveFilter]
    list_display = ["id", "post_num", "created_at", "is_approved"]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).filter(deleted_at__isnull=True)
