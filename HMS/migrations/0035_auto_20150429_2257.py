# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0034_auto_20150429_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurse',
            name='years_experience',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 30, 4, 57, 16, 775650, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 30, 3, 57, 16, 775650, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
