from django.urls import path
from . import views
router = DefaultRouter()
router.register(r'trainees', TraineeViewSet)
urlpatterns = [
    path('courses/', Course_List_Create.as_view(), name='course-list-create')
    path('courses/<int:pk>/', Course_Retrieve_Update_Delete.as_view(), name='course-retrieve-update-delete'),
    path('', include(router.urls)),
]