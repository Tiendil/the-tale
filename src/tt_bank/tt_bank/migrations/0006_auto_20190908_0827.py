# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-09-08 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt_bank', '0005_transaction_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='amount',
            field=models.BigIntegerField(),
        ),
    ]
