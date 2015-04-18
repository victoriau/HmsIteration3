# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0018_auto_20150417_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='id',
        ),
        migrations.AddField(
            model_name='bill',
            name='released',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 1, 55, 43, 600240, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 0, 55, 43, 600240, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='patient',
            field=models.OneToOneField(to='HMS.Patient', serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
