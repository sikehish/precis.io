# Generated by Django 4.1.1 on 2022-11-07 17:04

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('website', models.URLField()),
                ('profile', models.TextField()),
                ('location', models.CharField(max_length=30)),
                ('skills', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), size=None)),
                ('employers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), size=3)),
                ('titles', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), size=3)),
                ('job_start', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=3)),
                ('job_end', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=3)),
                ('degrees', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), size=3)),
                ('institutions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), size=3)),
                ('edu_start', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=3)),
                ('edu_end', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=3)),
                ('createdat', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]