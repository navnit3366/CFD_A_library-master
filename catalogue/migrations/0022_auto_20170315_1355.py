# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0021_auto_20170314_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
