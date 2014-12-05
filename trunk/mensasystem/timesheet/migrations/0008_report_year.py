# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0007_auto_20140929_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='year',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
