from rest_framework import serializers
from .models import *


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ["id", "content", "contact", "image"]


class SuggestioniAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = "__all__"
