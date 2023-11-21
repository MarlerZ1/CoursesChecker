from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Task(models.Model):
    number = models.PositiveIntegerField(default=111, validators=[MinValueValidator(111), MaxValueValidator(999)])
    name = models.CharField(max_length=256)
    description = models.TextField()

    def getDescription(self) -> str:
        size = 128
        if len(self.description) > size:
            return self.description[:128] + "..."
        else:
            return self.description

    def getNumber(self) -> int:
        return self.number

    def __str__(self):
        return str(self.number) + " " + str(self.name)

class Feedback(models.Model):
    work = models.ForeignKey(to='students.Work', on_delete=models.CASCADE,null=True, blank=True)

    proposedSolution = models.TextField()
    mistakeDescription = models.TextField()
    def __str__(self):
        return str(self.work.student.group) + " | " + str(self.work.student) + " | " + str(self.work.task)