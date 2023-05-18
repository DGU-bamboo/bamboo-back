from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, mixins
from .models import *
from .serializers import *
from django.db.models import Count
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action


class PostViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PostDetailSerializer
        return PostSerializer

    def get_queryset(self):
        return Post.objects.annotate(report_cnt=Count("report"))


class CommentViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Comment.objects.filter(is_approved=True).order_by("approved_at")
    serializer_class = CommentSerializer

    @action(methods=["GET"], detail=True, permission_classes=[IsAdminUser])
    def reject(self, request, *args, **kwargs):
        comment = self.get_object()
        comment.is_approved = False
        comment.save(update_fields=["is_approved"])
        return Response()
