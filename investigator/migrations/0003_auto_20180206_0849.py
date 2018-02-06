# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investigator', '0002_auto_20180206_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bankCard',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
