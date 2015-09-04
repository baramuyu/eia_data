# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0003_metacategory_seriesid'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriesid',
            name='category_id2',
            field=models.ForeignKey(related_name='category2', to='graphs.MetaCategory', null=True),
        ),
        migrations.AlterField(
            model_name='seriesid',
            name='category_id1',
            field=models.ForeignKey(related_name='category1', to='graphs.MetaCategory', null=True),
        ),
    ]
