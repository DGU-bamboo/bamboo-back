from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser


from .models import *
from .serializers import *


class SuggestionView(APIView):
    def post(self, request):
        serializers = SuggestionSerializer(Suggestion.objects.all(), many=True)
        return Response(serializers.data)
