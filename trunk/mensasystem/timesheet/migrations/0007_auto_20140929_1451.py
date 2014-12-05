# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0006_auto_20140929_1417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timesheet',
            old_name='noon_time_end',
            new_name='afternoon_time_end',
        ),
        migrations.RenameField(
            model_name='timesheet',
            old_name='noon_time_start',
            new_name='afternoon_time_start',
        ),
        migrations.AlterField(
            model_name='timesheetmoney',
            name='method',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'*', b'*'), (b'+', b'+')]),
        ),
    ]
