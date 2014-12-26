# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemIP',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('start_ip', models.IPAddressField()),
                ('end_ip', models.IPAddressField()),
            ],
            options={
                'verbose_name_plural': 'Management IP',
            },
            bases=(models.Model,),
        ),
    ]
