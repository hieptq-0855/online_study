from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=200)
    time = models.IntegerField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
