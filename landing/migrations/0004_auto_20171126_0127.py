# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 01:27
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_landing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landing',
            name='template_file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/landing', location='/home/dmitry/Projects/Python/django/filingroup/landing/templates/landing'), upload_to='', verbose_name='Template file (HTML file)'),
        ),
    ]
