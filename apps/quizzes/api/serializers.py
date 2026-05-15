from rest_framework import serializers

from ..models import Quiz, Question


class QuestionPostSerializer(serializers.ModelSerializer):
    """
    Serializer for Question model.
    """
    class Meta:
        model = Question
        fields = ['id', 'question_title', 'question_options',
                  'answer', 'created_at', 'updated_at']


class QuizPostSerializer(serializers.ModelSerializer):
    """
    Serializer for Quiz model.
    Includes nested questions.
    Accepts a YouTube URL as input to generate quizzes.
    """
    questions = QuestionPostSerializer(many=True, read_only=True)
    url = serializers.URLField(write_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at',
                  'updated_at', 'video_url', 'url', 'questions']
        
    def create(self, validated_data):
        """
        Override create method to set video_url from the 'url' field.
        """
        video_url = validated_data.pop('url')
        validated_data['video_url'] = video_url
        return super().create(validated_data)


class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer for Question model.
    """
    class Meta:
        model = Question
        fields = ['id', 'question_title', 'question_options',
                  'answer']


class QuizSerializer(serializers.ModelSerializer):
    """
    Serializer for Quiz model.
    Includes nested questions.
    Accepts a YouTube URL as input to generate quizzes.
    """
    questions = QuestionSerializer(many=True, read_only=True)
    url = serializers.URLField(write_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at',
                  'updated_at', 'video_url', 'url', 'questions']
        
    def create(self, validated_data):
        """
        Override create method to set video_url from the 'url' field.
        """
        video_url = validated_data.pop('url')
        validated_data['video_url'] = video_url
        return super().create(validated_data)