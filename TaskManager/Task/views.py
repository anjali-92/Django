'''
curl -X POST -d "username=admin&password=admin" http://10.55.125.8:8000/api-token-auth/
http POST 10.55.125.8:8000/api-token-auth/ username='admin' password='admin'

curl -X GET -H 'Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwidXNlcl9pZCI6MSwiZW1haWwiOiJhZG1pbkBhZG1pbi5jb20iLCJleHAiOjE0NjAwMTQ0ODl9.QHb8gY4yM1nLDs46lGP8u8lqFo1o8aevhoM1uqTSV9Q' http://10.55.125.8:8000/task/todolist/
'''

from Task.models import *
from Task.serializers import *
from rest_framework import generics
from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

def task_creator(self,status):
    user = self.request.user
    if user.id:
	print "get queryset"
	return Task.objects.filter(creator=user,status=status)
    else:
	return

class UserList(generics.ListAPIView):
    quertset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ToDoTaskList(generics.ListCreateAPIView):
    #queryset = Task.objects.filter(status='T')
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
	return task_creator(self,'T')
    
    def perform_create(self, serializer):
	serializer.save(creator=self.request.user)

class TaskList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
	return task_creator(self,self.kwargs['status'])

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def delete(self,request,*args,**kwargs):
	import ipdb;
	ipdb.set_trace()
	pk = kwargs['pk']
	task = Task.objects.filter(pk=int(pk))
	if task[0].status == 'T':
	    return super(TaskDetail,self).delete(self,request,*args,**kwargs)
	else:
	    content = {'warning': 'u cant delete inprogress/completed task'}
	    return Response(content, status=status.HTTP_304_NOT_MODIFIED)

    '''
    class ToDoTaskDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


    class InProgressTaskList(generics.ListAPIView):
	serializer_class = TaskSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
	    return task_creator(self,'I')

    class InProgressTaskDetail(generics.RetrieveUpdateAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class CompletedTaskList(generics.ListAPIView):
	serializer_class = TaskSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
	    return task_creator(self,'C')

    class CompletedTaskDetail(generics.RetrieveUpdateAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    '''	
