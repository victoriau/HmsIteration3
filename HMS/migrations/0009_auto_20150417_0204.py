# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0008_auto_20150416_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('startTime', models.DateTimeField(default=datetime.datetime(2015, 4, 17, 7, 4, 22, 744424, tzinfo=utc))),
                ('endTime', models.DateTimeField(default=datetime.datetime(2015, 4, 17, 8, 4, 22, 744424, tzinfo=utc))),
                ('doctor', models.ForeignKey(default=1, to='HMS.Doctor')),
                ('patient', models.ForeignKey(default=1, to='HMS.Patient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='birth_date',
            field=models.DateField(default=datetime.date(2015, 4, 17)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 4, 17)),
            preserve_default=True,
        ),
    ]
