# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0009_auto_20150903_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('name', models.CharField(max_length=2, serialize=False, primary_key=True)),
            ],
        ),
    ]
