from django.shortcuts import render
from rest_framework import mixins, status

from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class CommonReportViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CommonReport.objects.all()
    serializer_class = CommonReportSerializer

    def get_serializer_class(self):
        if self.action in ["create"]:
            return CommonReportCreateSerializer
        return CommonReportSerializer

    def perform_create(self, serializer):
        question_id = self.request.data["question"]
        answer = self.request.data["answer"]

        try:
            is_student = False
            question = Question.objects.get(id=question_id)
            if question.answer == answer:
                is_student = True
        except Exception:
            raise ValidationError()

        serializer.save(
            is_student=is_student,
            filtered_content=serializer.validated_data.get("content"),
        )

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [IsAdminUser()]
        return super().get_permissions()

    @action(methods=["PATCH"], detail=True, permission_classes=[IsAdminUser])
    def approve(self, request, *args, **kwargs):
        common = self.get_object()
        common.approve = True
        new_post = Post.objects.create(
            type="COMMON", content=common.filtered_content, is_student=common.is_student
        )
        common.post = new_post
        common.save(update_fields=["is_approve", "post"])
        serializer = self.get_serializer(common)
        return Response(serializer.data)

    @action(methods=["PATCH"], detail=True, permission_classes=[IsAdminUser])
    def reject(self, request, *args, **kwargs):
        report = self.get_object()
        report.is_approve = False
        report.save(update_fields=["is_approve"])
        return Response()


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
            return QuestionWithoutAnswerSerializer
        else:
            return QuestionSerializer

    def get_permissions(self):
        if self.action in ["create", "list", "retrieve", "update", "destroy"]:
            return [IsAdminUser()]
        return super().get_permissions()

    @action(methods=["GET"], detail=False)
    def random(self, request):
        question = Question.objects.order_by("?").first()
        serializer = QuestionWithoutAnswerSerializer(question)
        return Response(serializer.data)
