# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0002_auto_20160202_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='to_user',
            field=models.ForeignKey(related_name=b'invitation_received', verbose_name=b'user to invite', to=settings.AUTH_USER_MODEL),
        ),
    ]
