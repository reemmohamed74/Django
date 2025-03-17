from django.urls import path
from .views import course_list , delete_course
urlpatterns = [
    path('', course_list, name='trainee_list'),
    path('delete/<int:course_id>/', delete_course, name='delete_course'),
]