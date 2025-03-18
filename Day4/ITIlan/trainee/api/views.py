from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Trainee
from serializers import TraineeSerializer
class TraineeListCreateView(APIView):
    def get(self, request):
        trainees = Trainee.getallactivetrainee()
        serializer = TraineeSerializer(trainees)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TraineeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TraineeUpdateView(generics.UpdateAPIView):
    queryset = Trainee.getallactivetrainee()
    serializer_class = TraineeSerializer

class TraineeDeleteView(generics.DestroyAPIView):
    queryset = Trainee.getallactivetrainee()
    serializer_class = TraineeSerializer
