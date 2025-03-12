from django.shortcuts import render , redirect
from .forms import Traineeform
from .models import Trainee
# Create your views here.
def add_trainee(req):
    if req.method =="POST":
        from = Traineeform(req.POST)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
    return render(req , 'trainee/add_trainee.html')
