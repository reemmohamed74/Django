from django.db import models
from django.contrib.auth.models import User
from course.models import Course
from django.utils import timezone
course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
# Create your models here.
class Trainee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
@classmethod
def getallactivetrainee(cls):
    return cls.objects.all()

@classmethod
def gettraineebyid(cls, pk):
    return cls.objects.filter(id=pk).first()