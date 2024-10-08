from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers
from .views import *

default_router = routers.SimpleRouter(trailing_slash=False)
default_router.register("posts", PostViewSet, basename="posts")


comment_router = routers.SimpleRouter(trailing_slash=False)
comment_router.register("comments", CommentViewSet, basename="comments")


urlpatterns = [
    path("", include(default_router.urls)),
    path("", include(comment_router.urls)),
]
