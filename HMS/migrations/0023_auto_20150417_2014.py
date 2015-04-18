# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0022_auto_20150417_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='id',
            field=models.AutoField(serialize=False, auto_created=True, default=1, primary_key=True, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 2, 14, 28, 676438, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 1, 14, 28, 676438, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='appointment',
            field=models.OneToOneField(to='HMS.Appointment'),
            preserve_default=True,
        ),
    ]
