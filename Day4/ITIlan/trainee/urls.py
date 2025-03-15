from django.urls import path
from . import views

urlpatterns = [
    path('trainees/', views.TraineeListView.as_view(), name='trainee-list'),
    path('trainees/add/', views.AddTraineeView.as_view(), name='add-trainee'),
    path('trainees/update/<int:pk>/', views.UpdateTraineeView.as_view(), name='update-trainee'),
    path('trainees/delete/<int:pk>/', views.DeleteTraineeView.as_view(), name='delete-trainee'),
]