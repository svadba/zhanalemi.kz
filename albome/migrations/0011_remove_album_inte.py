# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-16 10:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albome', '0010_album_inte'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='inte',
        ),
    ]
