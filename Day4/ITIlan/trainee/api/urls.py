from django.urls import path
from .views import TraineeListCreateView, TraineeUpdateView, TraineeDeleteView

urlpatterns = [
    path('', TraineeListCreateView.as_view(), name='trainee-list-create'),
    path('<int:pk>/', TraineeUpdateView.as_view(), name='trainee-update'),
    path('<int:pk>/delete/', TraineeDeleteView.as_view(), name='trainee-delete'),
]
