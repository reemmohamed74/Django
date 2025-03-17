from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from ..models import Course
from .serializers import CourseSerializer
from rest_framework import viewsets
from course.models import Trainee
from .serializers import CourseSerializer



class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class TraineeViewSet(viewsets.ModelViewSet):
    queryset = Trainee.objects.all()
    serializer_class = CourseSerializer