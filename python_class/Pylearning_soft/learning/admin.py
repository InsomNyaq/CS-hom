from django.contrib import admin

from .models import Lesson, Progress, QuizAttempt, QuizQuestion


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("order", "title", "level", "duration", "is_published")
    list_filter = ("level", "is_published")
    search_fields = ("title", "summary")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "lesson", "completed", "updated_at")
    list_filter = ("completed",)


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ("lesson", "order", "question", "answer")
    list_filter = ("lesson",)


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "score", "total", "created_at")
    list_filter = ("created_at",)
