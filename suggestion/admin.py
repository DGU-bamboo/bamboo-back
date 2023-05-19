from typing import Any
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.contrib import admin
from suggestion.models import Suggestion, MaintainerSuggestion


@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ["id", "short_content", "created_at", "contact"]

    def short_content(self, instance):
        return instance.content[:30]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).filter(deleted_at__isnull=True)


@admin.register(MaintainerSuggestion)
class MaintainerSuggestionAdmin(admin.ModelAdmin):
    readonly_fields = [
        "content",
        "contact",
    ]
    exclude = [
        "deleted_at",
    ]
    list_display = ["id", "short_content", "created_at", "contact"]

    def short_content(self, instance):
        return instance.content[:30]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).filter(deleted_at__isnull=True)
