from django import forms
forms .models import Course
class Courseform(forms.ModelForm):
    class Meta :
        model = Course
        fields =['name' , 'description']