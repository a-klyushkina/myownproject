# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waiters', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='waiterprofile',
            old_name='first_name',
            new_name='name',
        ),
    ]