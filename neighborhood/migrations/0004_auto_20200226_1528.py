# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-26 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0003_auto_20200226_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='hood_pic',
            field=models.ImageField(default='img/jaba.jpg', upload_to='images/'),
        ),
    ]