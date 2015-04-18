# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0014_auto_20150417_0229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('releaseDate', models.DateField(default=datetime.date(2015, 4, 17))),
                ('dueDate', models.DateField(default=datetime.date(2015, 5, 17))),
                ('amount', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=9)),
                ('status', models.CharField(max_length=8, default='', choices=[('P', 'Paid'), ('D', 'Due'), ('O', 'Overdue')])),
                ('appointment', models.ForeignKey(to='HMS.Appointment', default=1)),
                ('patient', models.ForeignKey(to='HMS.Patient', default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 1, 6, 50, 434007, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 0, 6, 50, 434007, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
