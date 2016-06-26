# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-13 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('telefone1', models.CharField(max_length=20)),
                ('telefone2', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('endereco', models.TextField(blank=True)),
                ('dtnasc', models.DateField()),
                ('obs', models.TextField(blank=True)),
            ],
        ),
    ]
