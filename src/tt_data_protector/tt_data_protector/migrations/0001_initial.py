# Generated by Django 2.2.8 on 2020-05-10 16:10

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('state', models.IntegerField()),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('completed_at', models.DateTimeField(null=True)),
                ('expire_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'reports',
            },
        ),
        migrations.CreateModel(
            name='SubReport',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=32)),
                ('state', models.IntegerField(db_index=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('report', models.ForeignKey(db_column='report', on_delete=django.db.models.deletion.CASCADE, to='tt_data_protector.Report')),
            ],
            options={
                'db_table': 'subreports',
            },
        ),
    ]
