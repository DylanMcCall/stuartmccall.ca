# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-15 07:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0025_auto_20190114_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliomedia',
            name='portfolio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='galleries.Portfolio'),
        ),
    ]
