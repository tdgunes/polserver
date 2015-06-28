# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0004_auto_20150628_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='beacon',
            name='name',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
    ]
