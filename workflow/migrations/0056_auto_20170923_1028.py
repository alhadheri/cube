# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-23 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0055_merge_20170921_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLevelFour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Admin Boundary 4')),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Admin Boundary 4',
                'verbose_name_plural': 'Admin Boundary 4',
            },
        ),
        migrations.CreateModel(
            name='AdminLevelTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Admin Boundary 2')),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Admin Boundary 2',
                'verbose_name_plural': 'Admin Boundary 2',
            },
        ),
        migrations.RenameModel(
            old_name='Province',
            new_name='AdminLevelOne',
        ),
        migrations.RemoveField(
            model_name='district',
            name='province',
        ),
        migrations.RemoveField(
            model_name='village',
            name='admin_3',
        ),
        migrations.RemoveField(
            model_name='village',
            name='district',
        ),
        migrations.RemoveField(
            model_name='adminlevelthree',
            name='district',
        ),
        migrations.RemoveField(
            model_name='country',
            name='organization',
        ),
        migrations.AlterField(
            model_name='historicalsiteprofile',
            name='district',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workflow.AdminLevelTwo'),
        ),
        migrations.AlterField(
            model_name='historicalsiteprofile',
            name='village',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workflow.AdminLevelThree'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='admin_level_three',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='site_level3', to='workflow.AdminLevelThree', verbose_name='Administrative Level 3'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.AdminLevelTwo', verbose_name='Administrative Level 2'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='village',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.AdminLevelThree', verbose_name='Administrative Level 4'),
        ),
        migrations.DeleteModel(
            name='District',
        ),
        migrations.DeleteModel(
            name='Village',
        ),
        migrations.AddField(
            model_name='adminleveltwo',
            name='adminlevelone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflow.AdminLevelOne', verbose_name='Admin Level 1'),
        ),
        migrations.AddField(
            model_name='adminlevelfour',
            name='adminlevelthree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.AdminLevelThree'),
        ),
        migrations.AddField(
            model_name='adminlevelfour',
            name='adminleveltwo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.AdminLevelTwo', verbose_name='Admin Boundary 3'),
        ),
        migrations.AddField(
            model_name='adminlevelthree',
            name='adminleveltwo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.AdminLevelTwo', verbose_name='Admin Level 2'),
        ),
    ]
