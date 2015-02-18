# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0004_auto_20150217_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='full_path',
            field=models.CharField(max_length=400, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='translationfile',
            name='full_path',
            field=models.CharField(max_length=400, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
    ]
