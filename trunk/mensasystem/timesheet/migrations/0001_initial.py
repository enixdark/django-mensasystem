# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.IntegerField(null=True, blank=True)),
                ('fines', models.DecimalField(default=0.0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('leave_days', models.IntegerField(default=0)),
                ('note', models.TextField(null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Report',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeSheet',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('morning_time_start', models.TimeField(null=True)),
                ('morning_time_end', models.TimeField(null=True)),
                ('noon_time_start', models.TimeField(null=True)),
                ('noon_time_end', models.TimeField(null=True)),
                ('note', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Time Working',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeSheetMoney',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('fines_company_late', models.DecimalField(default=0.0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('fines_home_early', models.DecimalField(default=0.0, null=True, max_digits=12, decimal_places=2, blank=True)),
                ('note', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Money',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeWorking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('working_date', models.DateField(null=True, blank=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True, choices=[(b'morning', b'morning'), (b'noon', b'noon'), (b'full', b'full')])),
                ('note', models.TextField(null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Working',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserTimeSheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('working_date', models.DateField(null=True)),
                ('time_in', models.TimeField(null=True, blank=True)),
                ('time_out', models.TimeField(null=True, blank=True)),
                ('level', models.SmallIntegerField(default=0, null=True, blank=True)),
                ('fines', models.IntegerField(default=0, null=True, blank=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True, choices=[(b'normal', b'normal'), (b'good', b'good'), (b'late', b'late')])),
                ('special', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Management Time User',
            },
            bases=(models.Model,),
        ),
    ]
