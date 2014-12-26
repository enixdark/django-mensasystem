# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20141007_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='systemip',
            old_name='end_ip',
            new_name='ip',
        ),
        migrations.RemoveField(
            model_name='systemip',
            name='start_ip',
        ),
    ]
