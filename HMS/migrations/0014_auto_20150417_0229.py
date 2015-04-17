# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0013_auto_20150417_0218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('startTime', models.DateTimeField(default=datetime.datetime(2015, 4, 17, 7, 29, 13, 906665, tzinfo=utc))),
                ('endTime', models.DateTimeField(default=datetime.datetime(2015, 4, 17, 8, 29, 13, 906665, tzinfo=utc))),
                ('doctor', models.ForeignKey(to='HMS.Doctor', default=1)),
                ('patient', models.ForeignKey(to='HMS.Patient', default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='patientappointment',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='appointments',
        ),
        migrations.DeleteModel(
            name='PatientAppointment',
        ),
    ]
