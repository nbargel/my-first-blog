# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-14 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='apodo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
