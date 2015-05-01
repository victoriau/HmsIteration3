# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0035_auto_20150429_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='release_paycheck',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nurse',
            name='release_paycheck',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 30, 5, 33, 50, 760542, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 30, 4, 33, 50, 760542, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
