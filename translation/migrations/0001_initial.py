# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                 serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('languages', models.ManyToManyField(to='translation.Language')),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=300)),
                ('project', models.ForeignKey(to='translation.Project')),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                serialize=False, auto_created=True, primary_key=True)),
                ('original_text', models.CharField(max_length=5000,
                                                   verbose_name='Text')),
                ('translated_text', models.CharField(max_length=5000,
                                    verbose_name='Translation')),
                ('status', models.CharField(max_length=20,
                verbose_name='Status', choices=[(b'not_translated', b'Not Translated'),
                (b'needs_review', b'Needs Review'), (b'reviewed', b'Reviewed')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TranslationFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=300)),
                ('project', models.ForeignKey(to='translation.Project')),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='translation',
            name='original_file',
            field=models.ForeignKey(to='translation.TranslationFile'),
            preserve_default=True,
        ),
    ]
