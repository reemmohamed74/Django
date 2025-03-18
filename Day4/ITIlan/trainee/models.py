from django.db import models

# Create your models here.
class Trainee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    @classmethod
    def getallactivetrainee(cls):
        return cls.objects.all()