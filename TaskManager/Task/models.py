from django.db import models
from django.contrib import auth

TASK_TYPE_CHOICES = (('R','Research'),('D','Development'),('D','Design'))
TASK_STATUS = (('T','ToDo'),('I','InProgress'),('C','Completed'))

class Task(models.Model):
    creator = models.ForeignKey('auth.User', related_name='task_creator')
    name = models.CharField(max_length = 20)
    task_type = models.CharField(max_length=1, default = 'D', choices=TASK_TYPE_CHOICES )
    duration_needed = models.IntegerField()
    status = models.CharField(max_length=1, default='T', choices=TASK_STATUS )
    note = models.CharField(max_length=50, null=True, blank=True )



