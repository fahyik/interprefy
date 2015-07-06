# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tbox', '0002_auto_20150625_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='language',
            field=models.CharField(max_length=2, choices=[(b'AR', b'Arabic'), (b'DA', b'Danish'), (b'DE', b'German'), (b'EL', b'Greek'), (b'EN', b'English'), (b'ES', b'Spanish'), (b'FA', b'Persian'), (b'FR', b'French'), (b'HI', b'Hindi'), (b'IT', b'Italian'), (b'PT', b'Portuguese'), (b'RU', b'Russian'), (b'SV', b'Swedish'), (b'ZH', b'Chinese')]),
        ),
    ]
