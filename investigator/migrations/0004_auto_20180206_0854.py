# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investigator', '0003_auto_20180206_0849'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='investigator',
        ),
    ]
