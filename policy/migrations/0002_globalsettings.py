# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
    ]
