# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='remote',
            field=models.CharField(default='', max_length=360),
            preserve_default=False,
        ),
    ]
