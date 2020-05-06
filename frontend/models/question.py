from django.db import models


class Question(models.Model):
    content = models.CharField(max_length=500)
    question_type = models.IntegerField(default=0)
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE)
