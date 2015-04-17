# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
import phonenumber_field.modelfields
import django.utils.timezone
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=255, verbose_name='e-mail', unique=True)),
                ('activation_key', models.CharField(blank=True, max_length=40)),
                ('key_expires', models.DateTimeField(default=datetime.date(2015, 4, 13))),
                ('first_name', models.CharField(max_length=20, default='')),
                ('last_name', models.CharField(max_length=20, default='')),
                ('birth_date', models.DateField(default=datetime.date(2015, 4, 13))),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(null=True, max_length=128)),
                ('gender', models.CharField(max_length=7, default='', choices=[('MAL', 'Male'), ('FEM', 'Female')])),
                ('marital_Status', models.CharField(max_length=10, default='', choices=[('SIN', 'Single'), ('MAR', 'Married')])),
                ('house_number', models.IntegerField(default=0)),
                ('street', models.CharField(max_length=30, default='')),
                ('city', models.CharField(max_length=20, default='')),
                ('state', models.CharField(max_length=20, default='', choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')])),
                ('zip_code', localflavor.us.models.USZipCodeField(max_length=10)),
                ('name', models.CharField(max_length=50, default='')),
                ('relation', models.CharField(max_length=20, default='')),
                ('primary_Phone', models.IntegerField(default=0)),
                ('secondary_Phone', models.IntegerField(default=0)),
                ('is_content_manager', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'MyUser',
                'verbose_name_plural': 'MyUsers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('myuser_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('department', models.CharField(max_length=30, default='', choices=[('PED', 'Pediatrics'), ('ONC', 'Oncology'), ('FAM', 'Family Practice'), ('EME', 'Emergency'), ('ORT', 'Orthopedics')])),
                ('medical_History', models.CharField(max_length=40, default='')),
                ('insurance_Provider', models.CharField(max_length=40, default='')),
                ('insurance_Policy_Number', models.IntegerField(default=0)),
                ('is_patient', models.BooleanField(default=True)),
                ('is_authenticated', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Patient',
            },
            bases=('HMS.myuser',),
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('myuser_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('department', models.CharField(max_length=30, default='', choices=[('PED', 'Pediatrics'), ('ONC', 'Oncology'), ('FAM', 'Family Practice'), ('EME', 'Emergency'), ('ORT', 'Orthopedics')])),
                ('is_nurse', models.BooleanField(default=True)),
                ('is_authenticated', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Nurse',
            },
            bases=('HMS.myuser',),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('myuser_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('degree', models.CharField(max_length=40, default='MD', choices=[('MD', 'M.D.'), ('DO', 'D.O.')])),
                ('specialty', models.CharField(max_length=30, default='', choices=[('PED', 'Pediatrics'), ('ONC', 'Oncology'), ('FAM', 'Family Practice'), ('EME', 'Emergency'), ('ORT', 'Orthopedics')])),
                ('experience', models.CharField(max_length=60, default='')),
                ('is_doctor', models.BooleanField(default=True)),
                ('is_authenticated', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Doctor',
            },
            bases=('HMS.myuser',),
        ),
    ]
