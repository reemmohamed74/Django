from django.db import models

# Create your models here.
class Trainee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True)
    deleted = models.BooleanField(default=False)
    image = models.ImageField(upload_to='trainee/images' , null=True)


