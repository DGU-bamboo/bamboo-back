from rest_framework import serializers
from .models import *


class RandomQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "content"]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "answer"]
