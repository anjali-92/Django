from django.db import models

TASK_TYPE_CHOICES = (('R','Research'),('D','Development'),('D','Design'))
TASK_STATUS = (('T','ToDo'),('I','InProgress'),('C','Completed'))

class Task(models.Model):
    name = models.CharField(max_length = 20,null=True, blank=True)
    task_type = models.CharField(max_length=1, default = 'D', choices=TASK_TYPE_CHOICES, null=True, blank=True )
    duration_needed = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=1, default='T', choices=TASK_STATUS, null=True, blank=True )
    note = models.CharField(max_length=50, null=True, blank=True )
