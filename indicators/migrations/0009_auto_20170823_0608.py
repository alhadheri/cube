# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0031_auto_20170823_0608'),
        ('indicators', '0008_auto_20170823_0242'),
    ]

    operations = [
        migrations.AddField(
            model_name='datacollectionfrequency',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workflow.Organization'),
        ),
        migrations.AddField(
            model_name='externalservice',
            name='default_global',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='externalservice',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workflow.Organization'),
        ),
        migrations.AddField(
            model_name='indicatortype',
            name='default_global',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='indicatortype',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workflow.Organization'),
        ),
        migrations.AddField(
            model_name='level',
            name='global_default',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='level',
            name='workflowlevel1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.WorkflowLevel1'),
        ),
        migrations.AddField(
            model_name='reportingperiod',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workflow.Organization'),
        ),
        migrations.AlterField(
            model_name='disaggregationtype',
            name='standard',
            field=models.BooleanField(default=False, verbose_name=b'Standard'),
        ),
    ]
