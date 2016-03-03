# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task',
        ),
        migrations.AlterField(
            model_name='task',
            name='duration_needed',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='note',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'T', max_length=1, null=True, blank=True, choices=[(b'T', b'ToDo'), (b'I', b'InProgress'), (b'C', b'Completed')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.CharField(default=b'D', max_length=1, null=True, blank=True, choices=[(b'R', b'Research'), (b'D', b'Development'), (b'D', b'Design')]),
        ),
    ]
