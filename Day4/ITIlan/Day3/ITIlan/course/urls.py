from django.urls import path
from .views import add_course , update_course ,delete_course , course_list

urlpatterns = [
    path('add/', add_course, name='add_course'),
    path('update/<int:pk>/', update_course, name='update_course'),
    path('delete/<int:pk>/', delete_course, name='delete_course'),
    path('course_list/', course_list, name='course_list'),
]

