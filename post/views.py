from rest_framework import viewsets, mixins
from .models import *
from .serializers import *
from django.db.models import Count
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response


class PostViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    def get_serializer_class(self):
        if self.action == "retrieve":
            return PostDetailSerializer
        return PostSerializer

    def get_queryset(self):
        return Post.objects.annotate(report_cnt=Count("report")).order_by("-id")

    @action(methods=["GET"], detail=True)
    def comments(self, request, *args, **kwargs):
        queryset = Comment.objects.filter(is_approved=True).order_by("approved_at")
        serializers = CommentSerializer(queryset, many=True)
        return Response(serializers.data)


class CommentViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(methods=["GET"], detail=True, permission_classes=[IsAdminUser])
    def reject(self, request, *args, **kwargs):
        comment = self.get_object()
        comment.is_approved = False
        comment.save(update_fields=["is_approved"])
        return Response()
