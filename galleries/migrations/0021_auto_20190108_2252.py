# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-09 06:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0020_auto_20190106_1410'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ['sort_order'], 'verbose_name': 'gallery', 'verbose_name_plural': 'galleries'},
        ),
        migrations.AddField(
            model_name='gallery',
            name='portfolio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='galleries.Portfolio'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='sort_order',
            field=models.IntegerField(blank=True, db_index=True, default=0, verbose_name='Sort'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='gallery',
            unique_together=set([('portfolio', 'slug')]),
        ),
    ]
