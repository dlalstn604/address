# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='home_number',
            field=models.TextField(blank=True, null=True),
        ),
    ]
