# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('wxAccounts', models.CharField(max_length=20)),
                ('wxName', models.CharField(max_length=20)),
                ('account', models.CharField(max_length=20)),
                ('passWord', models.CharField(max_length=20)),
                ('role', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=20)),
                ('img', models.CharField(max_length=200)),
                ('gender', models.IntegerField(default=0)),
                ('identity', models.CharField(max_length=20)),
                ('bankCard', models.CharField(max_length=50)),
                ('station', models.IntegerField(default=0)),
                ('telephone', models.CharField(max_length=20)),
                ('isValid', models.IntegerField(default=1)),
                ('comment', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'investigator',
            },
        ),
    ]
