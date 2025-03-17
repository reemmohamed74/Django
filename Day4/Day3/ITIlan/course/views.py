from django.shortcuts import render, redirect
from .forms import Courseform
from .models import Course
# Create your views here.
def add_course(request):
    if request.method == 'POST':
        form = Courseform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = Courseform()
    return render(request, 'course/add_course.html', {'form': form})

def update_course(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = Courseform(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = Courseform(instance=course)
    return render(request, 'course/update_course.html', {'form': form})

def delete_course(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return redirect('course_list')
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course_list.html', {'courses': courses})