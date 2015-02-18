# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0003_auto_20150217_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='save_path',
            field=models.CharField(max_length=300, verbose_name='Repository Path', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(default=b'new', max_length=10, choices=[(b'new', b'Not cloned'), (b'cloned', b'To Inspect PO files'), (b'inspected', b'Inspected'), (b'error', b'Error cloning')]),
            preserve_default=True,
        ),
    ]
