from rest_framework.routers import DefaultRouter
from django.urls import path , include
from . import views
from .views import *
from course.api.views import *
router = DefaultRouter()
router.register(r'trainees', TraineeViewSet)
urlpatterns = [
    path('courses/', CourseListCreate.as_view(), name='course-list') ,
    path('courses/<int:pk>/', CourseRetrieveUpdateDelete.as_view(), name='course-retrieve-update-delete'),
    path('', include(router.urls)),
]