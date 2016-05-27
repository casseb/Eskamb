# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-18 04:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Eskamb_App', '0004_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('aprovado', models.CharField(max_length=2)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eskamb_App.Categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eskamb_App.Usuario')),
            ],
        ),
    ]