# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20171115_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='skype',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Skype'),
        ),
    ]
