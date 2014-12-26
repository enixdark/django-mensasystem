# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0009_auto_20141002_1350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'verbose_name_plural': 'B\xe1o C\xe1o Theo Th\xe1ng'},
        ),
        migrations.AlterModelOptions(
            name='timesheet',
            options={'verbose_name_plural': 'Qu\u1ea3n L\xed Ng\xe0y L\xe0m Vi\u1ec7c'},
        ),
        migrations.AlterModelOptions(
            name='timesheetmoney',
            options={'verbose_name_plural': 'Ti\u1ec1n Ph\u1ea1t'},
        ),
        migrations.AlterModelOptions(
            name='timeworking',
            options={'verbose_name_plural': 'Ngh\u1ec9 Vi\u1ec7c'},
        ),
        migrations.AlterModelOptions(
            name='usertimesheet',
            options={'verbose_name_plural': 'Ng\xe0y L\xe0m Vi\u1ec7c Nh\xe2n Vi\xean'},
        ),
    ]
