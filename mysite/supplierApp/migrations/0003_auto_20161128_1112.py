# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-28 11:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplierApp', '0002_auto_20161128_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='system',
            old_name='system_volume_per_system',
            new_name='system_volume_per_unit',
        ),
    ]
