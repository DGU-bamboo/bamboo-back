from django.urls import path
from .views import *

app_name = "suggestion"
urlpatterns = [
    path("api/suggestion/", SuggestionView.as_view()),
]
