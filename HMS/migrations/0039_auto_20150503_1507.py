# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0038_auto_20150503_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 21, 7, 34, 570291, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 20, 7, 34, 570291, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='gender',
            field=models.CharField(max_length=30, default='', choices=[('MAL', 'Male'), ('FEM', 'Female')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='marital_Status',
            field=models.CharField(max_length=30, default='', choices=[('SIN', 'Single'), ('MAR', 'Married')]),
            preserve_default=True,
        ),
    ]
