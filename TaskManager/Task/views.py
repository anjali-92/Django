from Task.models import *
from Task.serializers import *
from rest_framework import generics

class ToDoTaskList(generics.ListCreateAPIView):
    queryset = Task.objects.filter(task_type='T')
    serializer_class = TaskSerializer

class ToDoTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.filter(task_type='T')
    serializer_class = TaskSerializer

class InProgressTaskList(generics.ListAPIView):
    queryset = Task.objects.filter(task_type='I')
    serializer_class = TaskSerializer

class InProgressTaskDetail(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.filter(task_type='I')
    serializer_class = TaskSerializer

class CompletedTaskList(generics.ListAPIView):
    queryset = Task.objects.filter(task_type='C')
    serializer_class = TaskSerializer

class CompletedTaskDetail(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.filter(task_type='C')
    serializer_class = TaskSerializer
