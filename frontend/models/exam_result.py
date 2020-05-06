from django.db import models


class ExamResult(models.Model):
    result = models.CharField(max_length=200)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE)
