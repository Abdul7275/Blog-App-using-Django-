# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-08 12:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0003_auto_20170708_1725'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='clog',
            new_name='blog',
        ),
    ]
