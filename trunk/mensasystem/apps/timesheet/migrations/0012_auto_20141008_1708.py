# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0011_timesheetmoney_block'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timesheet',
            options={'verbose_name_plural': 'Qu\u1ea3n L\xed Th\u1eddi Gian L\xe0m Vi\u1ec7c'},
        ),
        migrations.AlterModelOptions(
            name='timeworking',
            options={'verbose_name_plural': 'Ng\xe0y Ngh\u1ec9'},
        ),
        migrations.AlterModelOptions(
            name='usertimesheet',
            options={'verbose_name_plural': 'Qu\u1ea3n L\xed Ng\xe0y L\xe0m Vi\u1ec7c'},
        ),
        migrations.AddField(
            model_name='timesheetmoney',
            name='fines_not_checkin',
            field=models.DecimalField(default=0.0, null=True, max_digits=12, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='timesheetmoney',
            name='fines_not_checkout',
            field=models.DecimalField(default=0.0, null=True, max_digits=12, decimal_places=2, blank=True),
            preserve_default=True,
        ),

    ]
