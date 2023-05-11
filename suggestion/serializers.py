from rest_framework import serializers
from .models import Suggestion


class SuggestionSerializer(serializers.Serializer):
    image = serializers.ImageField(use_url=True)
    content = serializers.CharField()
    contact = serializers.CharField()

    class Meta:
        model = Suggestion
        fields = "__all__"
