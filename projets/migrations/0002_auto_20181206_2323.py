# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-06 23:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projets', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projet',
            new_name='projets',
        ),
    ]