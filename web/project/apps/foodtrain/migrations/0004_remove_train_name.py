# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-10 12:33
from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtrain', '0003_auto_20161110_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train',
            name='name',
        ),
    ]
