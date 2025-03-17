from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseListView.as_view(), name='course-list'),
    path('courses/add/', views.AddCourseView.as_view(), name='add-course'),
]