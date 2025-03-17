from django.shortcuts import render, redirect
from django.http import HttpResponse

trainees = [
    'Ahmed',
      'Mohamed',
     'Ali'
]

def trainee_list(request):
    return render(request, 'trainee_list.html', {'trainees': trainees})

def add_trainee(request):
    if request.method == 'POST':
        trainee_name = request.POST.get('name')

        trainees.append(trainee_name)
        return redirect('trainee_list')

    return render(request, 'add_trainee.html')



def delete_trainee(request, id):
    try:

        trainee_to_delete = trainees[id]
        trainees.remove(trainee_to_delete)
        return redirect('trainee_list')
    except IndexError:
        return render(request, 'delete_trainee.html', {'error': 'Trainee not found'})