# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0024_auto_20150417_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 2, 18, 9, 497966, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 1, 18, 9, 497966, tzinfo=utc)),
            preserve_default=True,
        ),
    ]