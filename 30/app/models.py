from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=100)
    birthday = models.DateField()
    job = models.ForeignKey('Job', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
