# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0005_auto_20140929_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheetmoney',
            name='exp',
            field=models.DecimalField(default=0.0, null=True, max_digits=3, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='timesheetmoney',
            name='method',
            field=models.CharField(max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
    ]
