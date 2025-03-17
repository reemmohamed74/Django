from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('', views.trainee_list, name='trainee_list'),
    path('list/', views.trainee_list, name='trainee_list'),
    path('add/', views.add_trainee, name='trainee_add'),
    path('delete/<int:id>/', views.delete_trainee, name='delete_trainee'),

]

