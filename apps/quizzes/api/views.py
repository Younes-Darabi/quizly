from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import json

from ..models import Question, Quiz
from .serializers import QuizGetSerializer, QuizPostSerializer
from .services import Services
from .permissions import IsOwner


class QuizzesView(viewsets.ModelViewSet):
    """
    ViewSet to handle CRUD operations for Quizzes.
    Only authenticated users can access their own quizzes.
    """
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Quiz.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return QuizPostSerializer
        return QuizGetSerializer 

    def create(self, request, *args, **kwargs):
        """
        Handle POST request to create a new Quiz from a YouTube URL.
        1. Validates URL.
        2. Downloads audio and converts it to text.
        3. Generates questions using AI.
        4. Creates Quiz and Question objects in the database.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        URL = serializer.validated_data.get('url')

        if "youtu.be/" not in URL and "youtube.com/watch?v=" not in URL:
            return Response({"url": "YouTube link is not valid"}, status=status.HTTP_400_BAD_REQUEST)

        URL = Services.make_standard_link(URL)
        AUDIO = Services.download_file_from_youtube(URL)
        TEXT = Services.convert_audio_to_text(AUDIO)
        response = Services.make_questions_with_ai(TEXT)
        quiz_content = response.text
        quiz_data = json.loads(quiz_content)
        quiz = serializer.save(user=request.user)
        quiz.title = quiz_data.get("title")
        quiz.description = quiz_data.get("description")
        quiz.video_url = URL
        for q in quiz_data.get("questions", []):
            question = Question.objects.create(
                question_title=q["question_title"],
                question_options=q["question_options"],
                answer=q["answer"]
            )
            quiz.questions.add(question)
        quiz.save()

        output_serializer = QuizPostSerializer(quiz)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)
