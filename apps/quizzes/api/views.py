from rest_framework import viewsets

from ..models import Quiz
from .serializers import QuizSerializer


class QuizzesView(viewsets.ModelViewSet):

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
