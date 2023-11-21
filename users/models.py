from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Group(models.Model):

    groupName = models.CharField(max_length=4, null=False, blank=False)
    groupNumber = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(40)])
    groupYear = models.PositiveIntegerField(default=datetime.now().year)


    def __str__(self):
        return f'{self.groupName}-{str(self.groupNumber)}-{str(self.groupYear)}'


class User(AbstractUser):
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.last_name + " " + self.first_name
