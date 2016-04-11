from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name','task_type','duration_needed','status','note')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
	model = User
	fields = ('firstname', 'lastname', 'email')
