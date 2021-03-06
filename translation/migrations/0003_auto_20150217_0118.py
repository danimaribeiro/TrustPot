# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0002_project_remote'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(default=b'new', max_length=10, choices=[(b'new', b'Not cloned'), (b'cloned', b'To Inspect PO files'), (b'inspected', b'Inspected')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='remote',
            field=models.CharField(max_length=360, verbose_name='Url Remote Repository', blank=True),
            preserve_default=True,
        ),
    ]
