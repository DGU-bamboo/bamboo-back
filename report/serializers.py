from rest_framework import serializers
from .models import CommonReport, Question


class CommonReportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonReport
        fields = ["content", "password"]


class CommonReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonReport
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "content", "answer"]


class QuestionWithoutAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "content"]

