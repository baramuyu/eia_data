# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0006_auto_20150903_1008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seriesid',
            old_name='category1_id',
            new_name='category1',
        ),
        migrations.RenameField(
            model_name='seriesid',
            old_name='category2_id',
            new_name='category2',
        ),
        migrations.RenameField(
            model_name='seriesid',
            old_name='category3_id',
            new_name='category3',
        ),
        migrations.RenameField(
            model_name='seriesid',
            old_name='category4_id',
            new_name='category4',
        ),
        migrations.RenameField(
            model_name='seriesid',
            old_name='category5_id',
            new_name='category5',
        ),
        migrations.RenameField(
            model_name='seriesid',
            old_name='category6_id',
            new_name='category6',
        ),
        migrations.RenameField(
            model_name='seriesid',
            old_name='category7_id',
            new_name='category7',
        ),
        migrations.RenameField(
            model_name='seriesid',
            old_name='category8_id',
            new_name='category8',
        ),
        migrations.RenameField(
            model_name='seriesid',
            old_name='category9_id',
            new_name='category9',
        ),
    ]
