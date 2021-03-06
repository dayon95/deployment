# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data01', '0002_auto_20171109_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='posterdata',
            name='goods',
            field=models.TextField(default='default goods'),
        ),
        migrations.AddField(
            model_name='posterdata',
            name='how',
            field=models.TextField(default='default how'),
        ),
        migrations.AddField(
            model_name='posterdata',
            name='name',
            field=models.TextField(default='default name'),
        ),
        migrations.AddField(
            model_name='posterdata',
            name='theme',
            field=models.TextField(default='default theme'),
        ),
        migrations.AddField(
            model_name='posterdata',
            name='when',
            field=models.TextField(default='default when'),
        ),
        migrations.AddField(
            model_name='posterdata',
            name='where',
            field=models.TextField(default='default where'),
        ),
        migrations.AddField(
            model_name='posterdata',
            name='who',
            field=models.TextField(default='default who'),
        ),
        migrations.AlterField(
            model_name='posterdata',
            name='link',
            field=models.TextField(default='default link'),
        ),
        migrations.AlterField(
            model_name='posterdata',
            name='title',
            field=models.CharField(default='default title', max_length=10),
        ),
    ]
