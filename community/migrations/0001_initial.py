# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('categories', models.ManyToManyField(to='community.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=400)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('categories', models.ManyToManyField(to='community.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('categories', models.ManyToManyField(to='community.Category')),
                ('class_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.Type')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.Major')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='class_types',
            field=models.ManyToManyField(to='community.Type'),
        ),
        migrations.AddField(
            model_name='event',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.Club'),
        ),
        migrations.AddField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.User'),
        ),
        migrations.AddField(
            model_name='event',
            name='majors',
            field=models.ManyToManyField(to='community.Major'),
        ),
    ]
