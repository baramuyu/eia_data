# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0002_graph_votes'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaCategory',
            fields=[
                ('category_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Seriesid',
            fields=[
                ('series_id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('category_id1', models.ForeignKey(to='graphs.MetaCategory')),
            ],
        ),
    ]
