from django.contrib import admin
from .models import Quiz, Question

class QuestionInline(admin.TabularInline):
    model = Quiz.questions.through
    extra = 1
    verbose_name = "Question"
    verbose_name_plural = "Questions"

class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description', 'user__username', 'user__email']
    ordering = ['-created_at']

    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['question_title']
    ordering = ['-created_at']

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)