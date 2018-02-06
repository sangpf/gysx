# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('invId', models.IntegerField(default=None)),
                ('title', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=100)),
                ('client', models.CharField(max_length=200)),
                ('responsibility', models.CharField(max_length=200)),
                ('type', models.IntegerField(default=None)),
                ('status', models.IntegerField(default=None)),
                ('cTime', models.DateTimeField(db_column='cTime')),
                ('bTime', models.DateTimeField(db_column='bTime')),
                ('eTime', models.DateTimeField(db_column='eTime')),
                ('comment', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'project',
            },
        ),
    ]
