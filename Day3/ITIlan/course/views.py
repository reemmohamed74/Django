from django.shortcuts import render , redirect
from .forms import Courseform

# Create your views here.
def add_course(req):
    form = Courseform(req.POST)
    if form.is_valid():
        form.save()
        return redirect ('course_list')
    return render(req,'course/add_course.html')
