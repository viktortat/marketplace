# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0005_shop_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='slug',
            field=models.SlugField(help_text='used for create url', unique=True, verbose_name='slug'),
        ),
    ]
