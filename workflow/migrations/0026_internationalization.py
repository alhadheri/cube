# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 13:44
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0025_auto_20170817_0541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internationalization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=100, null=True, verbose_name='Language')),
                ('language_file', django.contrib.postgres.fields.jsonb.JSONField()),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('language',),
            },
        ),
    ]
