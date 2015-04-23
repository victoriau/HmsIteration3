# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0031_auto_20150417_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='billed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 23, 3, 6, 42, 797704, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 23, 2, 6, 42, 797704, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='dueDate',
            field=models.DateField(default=datetime.date(2015, 5, 22)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='releaseDate',
            field=models.DateField(default=datetime.date(2015, 4, 22)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='birth_date',
            field=models.DateField(default=datetime.date(2015, 4, 22)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 4, 22)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='primaryCareProvider',
            field=models.ForeignKey(null=True, default=1, to='HMS.Doctor', blank=True),
            preserve_default=True,
        ),
    ]
