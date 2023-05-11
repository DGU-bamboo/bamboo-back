from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class QuestionView(APIView):
    def get(self, request):
        question = Question.objects.order_by("?").first()
        serializer = RandomQuestionSerializer(question)
        return Response(serializer.data)


class AnswerView(APIView):
    def post(self, request):
        id = request.data.get("id")
        user_answer = request.data.get("answer")

        question = get_object_or_404(Question, id=id)
        answer = question.answer

        if answer == user_answer:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(
                {"오류": "정답이 일치하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST
            )
