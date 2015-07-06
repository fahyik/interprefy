# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tbox', '0005_session_name_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='name_id',
            field=models.CharField(max_length=50, null=True, editable=False),
        ),
    ]
