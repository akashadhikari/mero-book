# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-16 11:17
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0008_auto_20171205_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Class',
            field=models.IntegerField(default=7, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='details',
            name='Edition',
            field=models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Forth', 'Forth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth'), ('Seventh', 'Seventh'), ('Eighth', 'Eighth'), ('Ninth', 'Ninth'), ('Tenth', 'Tenth')], default='First', max_length=10),
        ),
        migrations.AlterField(
            model_name='details',
            name='Status',
            field=models.CharField(choices=[('Open', 'Open'), ('Reserved', 'Reserved')], default='Open', max_length=10),
        ),
        migrations.AlterField(
            model_name='details',
            name='Ward_number',
            field=models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(35), django.core.validators.MinValueValidator(1)]),
        ),
    ]
