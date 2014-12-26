# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0008_report_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertimesheet',
            old_name='time_in',
            new_name='check_in',
        ),
        migrations.RenameField(
            model_name='usertimesheet',
            old_name='time_out',
            new_name='check_out',
        ),
    ]
