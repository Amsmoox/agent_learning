from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.indexes import GinIndex

class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    baseline_understanding_pct = models.DecimalField(max_digits=5, decimal_places=2,
                                                   validators=[
                                                       MinValueValidator(0),
                                                       MaxValueValidator(100)
                                                   ])
    traits_json = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.student_id})"

    class Meta:
        indexes = [
            models.Index(fields=['student_id']),
            GinIndex(fields=['traits_json'])
        ]

class Quiz(models.Model):
    quiz_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    materials_json = models.JSONField(null=True, blank=True)
    questions_json = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.quiz_id})"

    class Meta:
        indexes = [
            models.Index(fields=['quiz_id']),
        ]

class SimAttempt(models.Model):
    attempt_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    run_label = models.CharField(max_length=100)
    comprehension_json = models.JSONField()
    answers_json = models.JSONField()
    total_score = models.SmallIntegerField()
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()

    def __str__(self):
        return f"Attempt {self.attempt_id} by {self.student.name}"

    class Meta:
        indexes = [
            models.Index(fields=['attempt_id']),
            models.Index(fields=['student']),
            models.Index(fields=['quiz']),
        ]
