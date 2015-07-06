# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conn_id', models.CharField(max_length=255)),
                ('conn_user', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('session_id', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=1, choices=[(b'A', b'Admin Room'), (b'B', b'Broadcast Room')])),
                ('language', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TokBox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_key', models.CharField(max_length=50)),
                ('api_secret', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('function', models.CharField(max_length=3, choices=[(b'Pub', b'Publisher'), (b'Sub', b'Subscriber'), (b'Mod', b'Moderator')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='connection',
            name='session',
            field=models.ForeignKey(to='tbox.Session'),
        ),
        migrations.AddField(
            model_name='connection',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
