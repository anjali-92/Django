# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('task_type', models.CharField(default=b'D', max_length=1, choices=[(b'R', b'Research'), (b'D', b'Development'), (b'D', b'Design')])),
                ('duration_needed', models.IntegerField()),
                ('status', models.CharField(default=b'T', max_length=1, choices=[(b'T', b'ToDo'), (b'I', b'InProgress'), (b'C', b'Completed')])),
                ('note', models.CharField(max_length=50, null=True, blank=True)),
                ('creator', models.ForeignKey(related_name='task_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
