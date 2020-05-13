from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    subjects = models.ManyToManyField('Subject')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
