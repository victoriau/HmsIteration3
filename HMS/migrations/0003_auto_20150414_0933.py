# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0002_auto_20150414_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='allergies',
            field=models.CharField(max_length=40, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='prescriptions',
            field=models.CharField(max_length=40, default=''),
            preserve_default=True,
        ),
    ]
