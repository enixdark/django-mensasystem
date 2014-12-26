# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0010_auto_20141007_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheetmoney',
            name='block',
            field=models.IntegerField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
