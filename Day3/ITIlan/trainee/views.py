from django.shortcuts import render, redirect
from .forms import Traineeform
from .models import Trainee
from course.models import Course
# Create your views here.

def add_trainee(request):
    if request.method == 'POST':
        form = Traineeform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            course = form.cleaned_data['course']
            trainee = Trainee(name=name, email=email, course=course)
            trainee.save()
            return redirect('trainee_list')
    else:
        form = Traineeform()

    return render(request, 'trainee/add_trainee.html', {'form': form})
def update_trainee(request, pk):
    trainee = Trainee.objects.get(id=pk)
    if request.method == 'POST':
        form = Traineeform(request.POST, instance=trainee)
        if form.is_valid():
            trainee.name = form.cleaned_data['name']
            trainee.email = form.cleaned_data['email']
            trainee.course = form.cleaned_data['course']
            trainee.save()
            return redirect('trainee_list')
    else:
        form = Traineeform(instance=trainee)

    return render(request, 'trainee/update_trainee.html', {'form': form})
def delete_trainee(request, pk):
    trainee = Trainee.objects.get(id=pk)
    trainee.delete()
    return redirect('trainee_list')


def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})
