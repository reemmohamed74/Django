from django.urls import path
from .views import add_trainee , update_trainee , delete_trainee , trainee_list

urlpatterns = [
    path('add/', add_trainee, name='add_trainee'),
    path('update/<int:pk>/', update_trainee, name='update_trainee'),
    path('delete/<int:pk>/' , delete_trainee, name='delete_trainee'),
    path('trainee_list/', trainee_list, name='trainee_list'),
]
