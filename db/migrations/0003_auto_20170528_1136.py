# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-28 11:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20170514_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyLanguages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_words', models.CharField(max_length=50)),
                ('wid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Words')),
            ],
            options={
                'db_table': 'daily_languages',
            },
        ),
        migrations.CreateModel(
            name='UserHabits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('value', models.CharField(max_length=26)),
                ('counts', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'user_habits',
            },
        ),
        migrations.RemoveField(
            model_name='toprelations',
            name='top1',
        ),
        migrations.RemoveField(
            model_name='toprelations',
            name='top2',
        ),
        migrations.RemoveField(
            model_name='toprelations',
            name='top3',
        ),
        migrations.RemoveField(
            model_name='toprelations',
            name='top4',
        ),
        migrations.RemoveField(
            model_name='toprelations',
            name='top5',
        ),
        migrations.RemoveField(
            model_name='toprelations',
            name='wid',
        ),
        migrations.DeleteModel(
            name='TopRelations',
        ),
        migrations.AlterUniqueTogether(
            name='userhabits',
            unique_together=set([('value', 'uid')]),
        ),
    ]
