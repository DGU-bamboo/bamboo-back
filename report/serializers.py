from rest_framework import serializers

from report.models import Question, Report
from django.shortcuts import get_object_or_404


class ReportSerializer(serializers.ModelSerializer):
    question = serializers.IntegerField(write_only=True)
    answer = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = Report
        fields = ["id", "type", "content", "password", "question", "answer"]

    def validate(self, data):
        question_id = data.pop("question")
        answer = data.pop("answer")
        try:
            question_instance = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise serializers.ValidationError("Question instance does not exist")
        data["is_student"] = question_instance.answer == answer
        return data

    def create(self, validated_data):
        validated_data["filtered_content"] = validated_data["content"]
        return super().create(validated_data)


class QuestionWithoutAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "content"]
