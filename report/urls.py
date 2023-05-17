from django.urls import path, include
from rest_framework import routers
from .views import ReportViewSet

default_router = routers.SimpleRouter(trailing_slash=False)
default_router.register("reports", ReportViewSet, basename="reports")


urlpatterns = [
    path("", include(default_router.urls)),
]
