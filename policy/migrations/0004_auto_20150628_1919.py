# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0003_policy_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.CharField(unique=True, max_length=36)),
            ],
        ),
        migrations.AlterField(
            model_name='policy',
            name='color',
            field=colorful.fields.RGBColorField(default=b'#123445', blank=True),
        ),
        migrations.AddField(
            model_name='policy',
            name='beacon',
            field=models.ForeignKey(default='', blank=True, to='policy.Beacon'),
            preserve_default=False,
        ),
    ]
