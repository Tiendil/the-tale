# Generated by Django 2.2.10 on 2020-05-20 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_delete_randompremiumrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='removed_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
