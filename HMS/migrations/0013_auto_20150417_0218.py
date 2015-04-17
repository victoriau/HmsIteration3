# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0012_auto_20150417_0211'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientAppointment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('startTime', models.DateTimeField(default=datetime.datetime(2015, 4, 17, 7, 18, 24, 437008, tzinfo=utc))),
                ('endTime', models.DateTimeField(default=datetime.datetime(2015, 4, 17, 8, 18, 24, 437008, tzinfo=utc))),
                ('doctor', models.ForeignKey(default=1, to='HMS.Doctor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patient',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.AddField(
            model_name='patient',
            name='appointments',
            field=models.ManyToManyField(to='HMS.PatientAppointment'),
            preserve_default=True,
        ),
    ]
