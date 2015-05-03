# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0037_auto_20150501_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 19, 46, 14, 494249, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 18, 46, 14, 494249, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='dueDate',
            field=models.DateField(default=datetime.date(2015, 6, 2)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='releaseDate',
            field=models.DateField(default=datetime.date(2015, 5, 3)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='birth_date',
            field=models.DateField(default=datetime.date(2015, 5, 3)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 5, 3)),
            preserve_default=True,
        ),
    ]
