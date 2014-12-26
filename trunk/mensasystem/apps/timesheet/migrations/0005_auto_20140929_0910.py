# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0004_auto_20140927_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertimesheet',
            name='fines',
            field=models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2, blank=True),
        ),
    ]
