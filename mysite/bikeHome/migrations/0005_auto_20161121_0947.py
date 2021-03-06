# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-21 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikeHome', '0004_auto_20161121_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='system',
            name='vehicle',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_1a',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_1b',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_1c',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_2a',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_2b',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_2c',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_3a',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_3b',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_3c',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_4a',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_4b',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_4c',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_5a',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_5b',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_5c',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_6a',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_6b',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_6c',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_7a',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_7b',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subsystem_7c',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='System',
        ),
    ]
