# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 01:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('abstract', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, db_index=True)),
                ('title', models.CharField(max_length=100)),
                ('caption', models.TextField(blank=True, max_length=200, null=True)),
                ('extra', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to=b'')),
                ('thumbnail', models.ImageField(blank=True, upload_to=b'')),
                ('link', models.URLField()),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galleries.Gallery')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]