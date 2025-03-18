from django.urls import path
from views import *

urlpatterns = [
    path('', TraineeListCreateView.as_view(), name='trainee-list-create'),
    path('update/<int:pk>/', TraineeUpdateView.as_view(), name='trainee-update'),
    path('delete/<int:pk>/', TraineeDeleteView.as_view(), name='trainee-delete'),
]