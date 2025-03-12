from django.db import models
from course.models import Course
# Create your models here.
class Trainee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="trainees")


