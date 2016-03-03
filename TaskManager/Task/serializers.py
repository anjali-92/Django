from rest_framework import serializers
from .models import *
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name','task_type','duration_needed','status','note')

