from rest_framework import serializers

from ..models import Quiz, Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'question_title', 'question_options',
                  'answer', 'created_at', 'updated_at']


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    url = serializers.URLField(write_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at',
                  'updated_at', 'video_url', 'url', 'questions']
        
    def create(self, validated_data):
        video_url = validated_data.pop('url')
        validated_data['video_url'] = video_url
        return super().create(validated_data)
