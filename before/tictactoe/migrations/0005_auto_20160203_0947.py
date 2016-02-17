# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0004_auto_20160203_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 3, 9, 47, 23, 200160), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='move',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 3, 9, 47, 23, 199432), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='move',
            name='x',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='move',
            name='y',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
    ]
