# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20171126_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='meta_description',
            field=models.TextField(null=True, verbose_name='SEO/Meta description'),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_title',
            field=models.CharField(max_length=250, null=True, verbose_name='SEO/Meta title'),
        ),
    ]
