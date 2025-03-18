from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from views import *

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)

urlpatterns = [
    path('', views.CourseViewSet.as_view({'get': 'list'}), name='courses-list'),
    path('<int:pk>/', views.CourseViewSet.as_view({'get': 'retrieve'}), name='course-detail'),
]
