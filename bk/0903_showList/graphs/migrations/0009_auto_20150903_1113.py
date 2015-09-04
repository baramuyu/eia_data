# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0008_auto_20150903_1035'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Seriesid',
            new_name='Scategory',
        ),
    ]
