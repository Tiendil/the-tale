# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-19 18:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0019_auto_20161127_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='cards',
        ),
    ]