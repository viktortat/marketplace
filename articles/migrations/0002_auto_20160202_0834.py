# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 05:34
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='announce',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default='', upload_to='articles', verbose_name='image'),
            preserve_default=False,
        ),
    ]