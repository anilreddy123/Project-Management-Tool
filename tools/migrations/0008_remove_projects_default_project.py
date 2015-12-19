# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0007_auto_20151204_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='default_project',
        ),
    ]
