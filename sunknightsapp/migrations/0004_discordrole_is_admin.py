# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-02 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunknightsapp', '0003_helpinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='discordrole',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
