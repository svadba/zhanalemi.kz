# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-03 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albome', '0003_auto_20170503_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100, verbose_name='название')),
                ('image', models.ImageField(upload_to='albome/photos', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(default=324324, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='albome.Album', verbose_name='альбом'),
            preserve_default=False,
        ),
    ]
