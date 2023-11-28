# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0022_auto_20170315_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='member_Name',
            field=models.CharField(blank=True, editable=False, max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='memberid',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]