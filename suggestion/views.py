from django.shortcuts import render
from rest_framework import mixins
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response


class SuggestionViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Suggestion.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve", "memo"]:
            return SuggestioniAdminSerializer
        else:
            return SuggestionSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [IsAdminUser()]
        return super().get_permissions()

    @action(methods=["POST"], detail=True, permission_classes=[IsAdminUser])
    def memo(self, request, *args, **kwargs):
        suggestion = self.get_object()
        memo = request.data.get("memo")
        suggestion.memo = memo
        suggestion.save(update_fields=["memo"])
        serializer = self.get_serializer(suggestion)
        return Response(serializer.data)
