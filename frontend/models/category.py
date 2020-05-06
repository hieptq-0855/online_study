from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    subjects = models.ManyToManyField('Subject')

    def __str__(self):
        return self.name
