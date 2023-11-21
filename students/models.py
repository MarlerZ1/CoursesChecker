from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

import users
from teachers.models import Task
from users.models import User


# Create your models here.

class Work(models.Model):
    student = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE)

    grade = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    isEvaluate = models.BooleanField(default=False)
    code = models.TextField()

    def __str__(self):
        return str(self.task)

