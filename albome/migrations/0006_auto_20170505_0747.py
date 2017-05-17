# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-05 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albome', '0005_auto_20170505_0630'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(default=23, upload_to='albome/photos', verbose_name='изображение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(max_length=150, null=True, verbose_name='Транслит'),
        ),
    ]
