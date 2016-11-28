# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-28 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikeHome', '0006_auto_20161128_0511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='supplier_1',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='supplier_2',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='supplier_3',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='supplier_4',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='supplier_5',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='supplier_6',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='supplier_7',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='system_1_supplier',
            field=models.CharField(choices=[('s1a', 'name#s1a'), ('s1b', 'name#s1b'), ('s1c', 'name#s1c')], default='s1a', max_length=3),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='system_2_supplier',
            field=models.CharField(choices=[('s2a', 'name#s2a'), ('s2b', 'name#s2b'), ('s2c', 'name#s2c')], default='s2a', max_length=3),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='system_3_supplier',
            field=models.CharField(choices=[('s3a', 'name#s3a'), ('s3b', 'name#s3b'), ('s3c', 'name#s3c')], default='s3a', max_length=3),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='system_4_supplier',
            field=models.CharField(choices=[('s4a', 'name#s4a'), ('s4b', 'name#s4b'), ('s4c', 'name#s4c')], default='s4a', max_length=3),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='system_5_supplier',
            field=models.CharField(choices=[('s5a', 'name#s5a'), ('s5b', 'name#s5b'), ('s5c', 'name#s5c')], default='s5a', max_length=3),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='system_6_supplier',
            field=models.CharField(choices=[('s6a', 'name#s6a'), ('s6b', 'name#s6b'), ('s6c', 'name#s6c')], default='s6a', max_length=3),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='system_7_supplier',
            field=models.CharField(choices=[('s7a', 'name#s7a'), ('s7b', 'name#s7b'), ('s7c', 'name#s7c')], default='s7a', max_length=3),
        ),
    ]