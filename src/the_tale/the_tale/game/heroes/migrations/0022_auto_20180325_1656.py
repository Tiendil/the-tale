# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-03-25 16:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0021_load_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='energy',
        ),
        migrations.RemoveField(
            model_name='hero',
            name='energy_bonus',
        ),
    ]
