from django.urls import path
from .views import *


app_name = "report"
urlpatterns = [
    path("api/report/random-question", QuestionView.as_view()),
    path("api/report/answer-question", AnswerView.as_view()),
]
