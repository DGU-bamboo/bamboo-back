from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers
from .views import *

question_router = routers.SimpleRouter(trailing_slash=False)
question_router.register("questions", QuestionViewSet, basename="questions")

urlpatterns = [
    path("", include(question_router.urls)),
]
