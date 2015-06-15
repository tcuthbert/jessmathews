# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=25)),
                ('slug', models.SlugField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('owner', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=25, unique=True)),
                ('date_created', models.DateField(default=django.utils.timezone.now, editable=False)),
                ('image', models.ImageField(upload_to='photos')),
                ('category', models.ManyToManyField(to='gallery.Category')),
            ],
        ),
    ]
