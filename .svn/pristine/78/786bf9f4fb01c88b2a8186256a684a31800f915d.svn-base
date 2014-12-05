# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0003_auto_20140927_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertimesheet',
            name='payment',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timeworking',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'morning', b'morning'), (b'noon', b'noon'), (b'full', b'full')]),
        ),
    ]
