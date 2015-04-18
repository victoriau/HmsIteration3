# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import django.core.validators
import datetime
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0017_auto_20150417_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='purpose',
            field=models.CharField(default='', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 1, 48, 19, 903416, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 0, 48, 19, 903416, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='amount',
            field=models.DecimalField(default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(0.0)], max_digits=9, decimal_places=2),
            preserve_default=True,
        ),
    ]
