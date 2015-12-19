# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0010_auto_20151208_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='user',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
        migrations.RemoveField(
            model_name='taskcomments',
            name='user',
        ),
    ]
