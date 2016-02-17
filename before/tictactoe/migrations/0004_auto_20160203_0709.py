# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0003_auto_20160202_0932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='move',
            options={'get_latest_by': 'timestamp'},
        ),
        migrations.RemoveField(
            model_name='invitation',
            name='time_stamp',
        ),
        migrations.AddField(
            model_name='invitation',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 3, 7, 9, 47, 954990), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='move',
            name='by_first_player',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='move',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 3, 7, 9, 47, 954400), auto_now_add=True),
            preserve_default=True,
        ),
    ]
