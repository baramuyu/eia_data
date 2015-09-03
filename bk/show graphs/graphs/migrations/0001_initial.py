# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('graph_id', models.AutoField(serialize=False, primary_key=True)),
                ('seriesid', models.CharField(max_length=50)),
                ('geosetid', models.CharField(max_length=50)),
                ('geomapping', models.BooleanField(default=False)),
                ('notes', models.TextField(default=b'', verbose_name=b'Notes', blank=True)),
                ('category', models.ForeignKey(to='graphs.Category')),
            ],
        ),
    ]
