from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


    @classmethod
    def get_courses(cls):
        return cls.objects.all()
