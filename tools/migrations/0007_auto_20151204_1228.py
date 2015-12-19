# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tools', '0006_team_team_creation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='team',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='username',
        ),
        migrations.AddField(
            model_name='projects',
            name='userid',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(related_name='user_assignedto', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taskcomments',
            name='username',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
