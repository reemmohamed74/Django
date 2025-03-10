from django.urls import path
from .views import trainee_list , delete_trainee
urlpatterns = [
    path('', trainee_list, name='trainee_list'),
    path('delete/<int:trainee_id>/', delete_trainee, name='delete_trainee'),
]