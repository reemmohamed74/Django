from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'homepage/home.html')
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')
