# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
                ('default_project', models.BooleanField(default=False)),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teamname', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=75)),
                ('firstname', models.CharField(max_length=20, null=True)),
                ('lastname', models.CharField(max_length=20, null=True)),
                ('designation', models.CharField(max_length=15, null=True)),
                ('password1', models.CharField(max_length=20, null=True)),
                ('password2', models.CharField(max_length=20, null=True)),
                ('team', models.ForeignKey(to='tools.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='taskcomments',
            name='username',
            field=models.ForeignKey(blank=True, to='tools.Users', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(related_name='user_assignedto', blank=True, to='tools.Users', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(blank=True, to='tools.Projects', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projects',
            name='username',
            field=models.ForeignKey(blank=True, to='tools.Users', null=True),
            preserve_default=True,
        ),
    ]
