from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import json

from ..models import Question, Quiz
from .serializers import QuizSerializer
from .services import Services


class QuizzesView(viewsets.ModelViewSet):

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        URL = serializer.validated_data.get('url')
        URL = Services.make_standard_link(URL)
        AUDIO = Services.download_file_from_youtube(URL)
        TEXT = Services.convert_audio_to_text(AUDIO)
        response = Services.make_questions_with_ai(TEXT)
        quiz_content = response.text
        quiz_data = json.loads(quiz_content)
        quiz = serializer.save()
        quiz.video_url = URL
        for q in quiz_data.get("questions", []):
            question = Question.objects.create(
                question_title=q["question_title"],
                question_options=q["question_options"],
                answer=q["answer"]
            )
            quiz.questions.add(question)
        quiz.save()

        output_serializer = QuizSerializer(quiz)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)