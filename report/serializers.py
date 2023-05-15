from rest_framework import serializers
from .models import CommonReport


class CommonReportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonReport
        fields = ["content", "password"]


class CommonReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonReport
        fields = "__all__"
