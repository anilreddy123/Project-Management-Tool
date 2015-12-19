# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0004_team_team_creation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_creation_date',
        ),
    ]
