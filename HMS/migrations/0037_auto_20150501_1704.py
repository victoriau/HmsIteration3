# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0036_auto_20150429_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 1, 23, 4, 46, 336270, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 1, 22, 4, 46, 336270, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='dueDate',
            field=models.DateField(default=datetime.date(2015, 5, 31)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='releaseDate',
            field=models.DateField(default=datetime.date(2015, 5, 1)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='birth_date',
            field=models.DateField(default=datetime.date(2015, 5, 1)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 5, 1)),
            preserve_default=True,
        ),
    ]
