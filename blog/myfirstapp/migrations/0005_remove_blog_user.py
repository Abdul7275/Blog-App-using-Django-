# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-08 12:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0004_auto_20170708_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='user',
        ),
    ]
