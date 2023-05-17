from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers
from .views import *


default_router = routers.SimpleRouter(trailing_slash=False)
default_router.register("commons", CommonReportViewSet, basename="commonreports")

question_router = routers.SimpleRouter(trailing_slash=False)
question_router.register("questions", QuestionViewSet, basename="questions")

urlpatterns = [
    path("", include(default_router.urls)),
    path("", include(question_router.urls)),
]
