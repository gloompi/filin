# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20171126_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='free_places',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Free places'),
        ),
    ]
