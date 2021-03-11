from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.QuestionAPIView.as_view()),
]