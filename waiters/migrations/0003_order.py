# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 10:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waiters', '0002_auto_20170530_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.CharField(max_length=2)),
                ('text', models.TextField(max_length=300)),
                ('remark', models.TextField(max_length=100)),
                ('status', models.CharField(max_length=30)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('waiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='waiters.waiterprofile')),
            ],
        ),
    ]
