from django.shortcuts import render
from rest_framework import mixins
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response


class QuestionViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Question.objects.all()

    def get_serializer_class(self):
        if self.action == "random":
            return RandomQuestionSerializer
        else:
            return QuestionSerializer

    def get_permissions(self):
        if self.action in ["create", "list", "retrieve", "update", "destroy"]:
            return [IsAdminUser()]
        return super().get_permissions()

    @action(methods=["GET"], detail=False)
    def random(self, request):
        question = Question.objects.order_by("?").first()
        serializer = RandomQuestionSerializer(question)
        return Response(serializer.data)
