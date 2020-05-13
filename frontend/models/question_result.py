from django.db import models


class QuestionResult(models.Model):
    is_correct = models.BooleanField()
    exam_result = models.ForeignKey('ExamResult', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choices = models.ManyToManyField('Choice')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
