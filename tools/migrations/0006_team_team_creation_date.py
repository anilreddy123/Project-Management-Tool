# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0005_remove_team_team_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
