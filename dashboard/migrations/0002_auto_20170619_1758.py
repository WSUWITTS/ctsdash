# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='building',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='room',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='room',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='date_modified',
        ),
        migrations.AddField(
            model_name='building',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='building',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='last modified'),
        ),
        migrations.AddField(
            model_name='room',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='last modified'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='last modified'),
        ),
    ]