from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE = [
        (1, 'Admin'),
        (0, 'Client'),
    ]

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mid_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=200)
    dob = models.DateField()
    role = models.IntegerField(choices=ROLE, default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.mid_name, self.last_name)
