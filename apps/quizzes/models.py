from django.db import models


class Question(models.Model):

    question_title = models.CharField(max_length=100)
    question_options = models.JSONField(default=list)
    answer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_title


class Quiz(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    video_url = models.CharField(max_length=200)
    questions = models.ManyToManyField(Question, related_name='questions')
    
    def __str__(self):
        return self.title
