# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-14 17:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_apodo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='apodo',
        ),
    ]
