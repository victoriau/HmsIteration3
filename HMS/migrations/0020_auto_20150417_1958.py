# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0019_auto_20150417_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 1, 58, 47, 412885, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 0, 58, 47, 412885, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='appointment',
            field=models.OneToOneField(serialize=False, primary_key=True, to='HMS.Appointment'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='patient',
            field=models.ForeignKey(to='HMS.Patient', default=1),
            preserve_default=True,
        ),
    ]
