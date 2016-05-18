# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-18 03:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Eskamb_App', '0003_contato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
                ('endRua', models.CharField(max_length=100)),
                ('endNumero', models.IntegerField()),
                ('endBairro', models.CharField(max_length=100)),
                ('endCidade', models.CharField(max_length=100)),
                ('endEstado', models.CharField(max_length=2)),
                ('endCep', models.CharField(max_length=100)),
                ('contato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eskamb_App.Contato')),
            ],
        ),
    ]
