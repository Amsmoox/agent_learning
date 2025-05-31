from django.contrib import admin
from django.contrib.postgres.fields import JSONField
from .models import Student, Quiz, SimAttempt

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'baseline_understanding_pct', 'created_at')
    search_fields = ('name', 'student_id')
    readonly_fields = ('student_id', 'created_at')

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('quiz_id', 'title', 'created_at')
    search_fields = ('title', 'quiz_id')
    readonly_fields = ('quiz_id', 'created_at')

@admin.register(SimAttempt)
class SimAttemptAdmin(admin.ModelAdmin):
    list_display = ('attempt_id', 'student', 'quiz', 'run_label', 'total_score', 'started_at', 'ended_at')
    list_filter = ('student', 'quiz', 'run_label')
    search_fields = ('attempt_id', 'run_label', 'student__name', 'quiz__title')
    readonly_fields = ('attempt_id',)