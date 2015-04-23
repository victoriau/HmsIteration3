# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0032_auto_20150422_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 23, 17, 54, 30, 948360, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 23, 16, 54, 30, 948360, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='dueDate',
            field=models.DateField(default=datetime.date(2015, 5, 23)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='releaseDate',
            field=models.DateField(default=datetime.date(2015, 4, 23)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='status',
            field=models.CharField(choices=[('Due', 'Due'), ('Paid', 'Paid'), ('Overdue', 'Overdue')], max_length=8, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='birth_date',
            field=models.DateField(default=datetime.date(2015, 4, 23)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 4, 23)),
            preserve_default=True,
        ),
    ]
