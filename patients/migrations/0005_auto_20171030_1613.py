# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_auto_20171030_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='therapy',
            name='diagnosis',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='therapy',
            name='physiotherapy',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]