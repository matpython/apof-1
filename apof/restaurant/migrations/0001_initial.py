# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('spice_rate', models.DecimalField(decimal_places=1, max_digits=5)),
                ('rank', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Ingridients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('open_current_day', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=10)),
                ('www', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant'),
        ),
        migrations.AddField(
            model_name='ingridients',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Meal'),
        ),
    ]