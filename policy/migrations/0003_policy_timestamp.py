# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0002_globalsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 23, 44, 40, 408433, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
