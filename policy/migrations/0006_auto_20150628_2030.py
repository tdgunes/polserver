# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0005_beacon_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='beacon',
            field=models.ForeignKey(blank=True, to='policy.Beacon', null=True),
        ),
    ]
