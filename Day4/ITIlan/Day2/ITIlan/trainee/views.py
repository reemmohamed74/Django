from django.shortcuts import render , redirect

# Create your views here.

from .models import Trainee
from django.http import HttpResponse

def add_trainee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        new_trainee = Trainee(name=name, email=email, phone=phone)
        new_trainee.save()
        return redirect('trainee_list')
    return render(request, 'trainee/add_trainee.html')


def updatetrainees(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        trainee = Trainee.objects.get(id=id)
        trainee.name = name
        trainee.email = email
        trainee.phone = phone
        trainee.save()

        return redirect('trainee_list')

    trainee = Trainee.objects.get(id=id)
    return render(request, 'trainee/update_trainee.html', {'trainee': trainee})


def trainee_list(request):
    active_trainees = Trainee.objects.filter(deleted=False)
    deleted_trainees = Trainee.objects.filter(deleted=True)
    return render(request, 'trainee/trainee_list.html', {
        'trainees': active_trainees,
        'deleted_trainees': deleted_trainees
    })
def delete_trainee(request , trainee_id ):
    trainee= Trainee.objects.get(id=trainee_id)
    trainee.deleted = True
    trainee.save()
    return redirect('trainee_list')


