# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-05-26 03:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publish',
            new_name='publish_id',
        ),
    ]
