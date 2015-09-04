# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0004_auto_20150903_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriesid',
            name='category_id3',
            field=models.ForeignKey(related_name='category3', to='graphs.MetaCategory', null=True),
        ),
        migrations.AddField(
            model_name='seriesid',
            name='category_id4',
            field=models.ForeignKey(related_name='category4', to='graphs.MetaCategory', null=True),
        ),
        migrations.AddField(
            model_name='seriesid',
            name='category_id5',
            field=models.ForeignKey(related_name='category5', to='graphs.MetaCategory', null=True),
        ),
        migrations.AddField(
            model_name='seriesid',
            name='category_id6',
            field=models.ForeignKey(related_name='category6', to='graphs.MetaCategory', null=True),
        ),
        migrations.AddField(
            model_name='seriesid',
            name='category_id7',
            field=models.ForeignKey(related_name='category7', to='graphs.MetaCategory', null=True),
        ),
        migrations.AddField(
            model_name='seriesid',
            name='category_id8',
            field=models.ForeignKey(related_name='category8', to='graphs.MetaCategory', null=True),
        ),
        migrations.AddField(
            model_name='seriesid',
            name='category_id9',
            field=models.ForeignKey(related_name='category9', to='graphs.MetaCategory', null=True),
        ),
    ]
