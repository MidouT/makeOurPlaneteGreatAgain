# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-06 23:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projets', '0002_auto_20181206_2323'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='projets',
            new_name='projet',
        ),
    ]
