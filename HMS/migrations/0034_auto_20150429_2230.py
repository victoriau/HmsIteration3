# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0033_auto_20150423_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='salary',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0.0)], decimal_places=2, default=Decimal('0.00'), max_digits=9),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctor',
            name='years_experience',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nurse',
            name='salary',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0.0)], decimal_places=2, default=Decimal('0.00'), max_digits=9),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 30, 4, 30, 14, 292798, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 30, 3, 30, 14, 292798, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='dueDate',
            field=models.DateField(default=datetime.date(2015, 5, 29)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='releaseDate',
            field=models.DateField(default=datetime.date(2015, 4, 29)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='birth_date',
            field=models.DateField(default=datetime.date(2015, 4, 29)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 4, 29)),
            preserve_default=True,
        ),
    ]
