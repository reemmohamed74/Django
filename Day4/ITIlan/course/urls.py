# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('courses/', views.CourseListView.as_view(), name='course-list'),
#     path('courses/add/', views.AddCourseView.as_view(), name='add-course'),
# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views import CourseViewSet


router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')


urlpatterns = [
    path('', include(router.urls)),
]

