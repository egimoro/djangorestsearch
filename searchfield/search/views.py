from rest_framework import generics, filters

from .models import Question
from .serializers import QuestionSerializer


class QuestionAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['question_text']