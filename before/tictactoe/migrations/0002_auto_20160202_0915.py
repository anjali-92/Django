# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tictactoe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=300, blank=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(related_name=b'invitation_sent', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(related_name=b'invitation_received', verbose_name=b'user to invite', to=settings.AUTH_USER_MODEL, help_text=b'Please select user to invite.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Active'), (b'F', b'First Player Wins'), (b'S', b'Second Player Wins'), (b'D', b'Draw')]),
            preserve_default=True,
        ),
    ]
