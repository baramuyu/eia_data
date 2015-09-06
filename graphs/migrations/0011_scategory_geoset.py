# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0010_states'),
    ]

    operations = [
        migrations.AddField(
            model_name='scategory',
            name='geoset',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
