# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0012_auto_20150906_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graph',
            name='category',
        ),
        migrations.DeleteModel(
            name='States',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Graph',
        ),
    ]
