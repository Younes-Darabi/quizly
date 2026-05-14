from django.contrib import admin

from .models import Quiz


class QuizAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'description', 'user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description', 'user__username', 'user__email']
    ordering = ['-created_at']


admin.site.register(Quiz, QuizAdmin)