# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tbox', '0006_auto_20150630_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='conn_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_id',
            field=models.CharField(unique=True, max_length=72),
        ),
    ]
