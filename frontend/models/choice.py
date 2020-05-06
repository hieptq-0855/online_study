from django.db import models


class Choice(models.Model):
    content = models.CharField(max_length=200)
    is_answer = models.BooleanField()
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
