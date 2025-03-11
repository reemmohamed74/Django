from django.urls import path
from . import views
from .views import *
#
# urlpatterns = [
#     path('list/', views.course_list, name='course_list'),  # قائمة الدورات
#     path('add/', views.add_course, name='course_add'),  # إضافة دورة
#     path('update/<int:id>/', views.update_course, name='course_update'),  # تحديث دورة
#     path('delete/<int:id>/', views.delete_course, name='course_delete'),  # حذف دورة
#
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('add/', views.add_course, name='course_add'),
    path('delete/<str:course_name>/', views.delete_course, name='delete_course'),
]
