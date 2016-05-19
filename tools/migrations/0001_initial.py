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
            name='Projects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_title', models.CharField(max_length=200)),
                ('project_description', models.CharField(max_length=3000)),
                ('duration', models.CharField(max_length=100, null=True, blank=True)),
                ('project_creation_date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('taskname', models.CharField(max_length=500)),
                ('task_desc', models.CharField(max_length=3000, null=True, blank=True)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('project', models.ForeignKey(blank=True, to='tools.Projects', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tcommencts', models.CharField(max_length=400)),
                ('tcommencts_reply', models.CharField(max_length=400, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(blank=True, to='tools.Task', null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
