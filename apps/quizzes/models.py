from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """
    Model representing a single quiz question.
    """
    question_title = models.CharField(max_length=100)
    question_options = models.JSONField(default=list)
    answer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_title


class Quiz(models.Model):
    """
    Model representing a quiz.
    A quiz belongs to a user and can contain multiple questions.
    """
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    video_url = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    questions = models.ManyToManyField(Question, related_name='quizzes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_quizzes")
    
    def __str__(self):
        return self.title
