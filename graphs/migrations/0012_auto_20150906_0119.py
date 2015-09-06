# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0011_scategory_geoset'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scategory',
            old_name='geoset',
            new_name='geoset_id',
        ),
    ]
