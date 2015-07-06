# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tbox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='session_id',
            field=models.CharField(max_length=72),
        ),
        migrations.AlterField(
            model_name='tokbox',
            name='api_key',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='tokbox',
            name='api_secret',
            field=models.CharField(max_length=40),
        ),
    ]
