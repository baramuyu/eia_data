# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0007_auto_20150903_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metacategory',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
