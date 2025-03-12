from django import forms
from course.models import Course
class Traineeform (forms.form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    course = forms.ModelChoiceField(selectedcourse=Course.objects.all())
