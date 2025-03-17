from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from .forms import RegisterForm
# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('course-list')
        return render(request, 'users/register.html', {'form': form})


