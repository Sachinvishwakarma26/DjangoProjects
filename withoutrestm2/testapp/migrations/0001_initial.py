# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-25 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('rollno', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('gf', models.CharField(max_length=64)),
                ('bf', models.CharField(max_length=64)),
            ],
        ),
    ]
