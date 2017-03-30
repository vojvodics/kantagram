# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 01:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Akcija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('photo', models.URLField()),
                ('location', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=200)),
                ('long_desc', models.TextField()),
                ('date', models.DateTimeField(blank=True)),
                ('votes', models.IntegerField(default=0)),
                ('successful', models.BooleanField(default=False)),
                ('update_image', models.URLField(blank=True)),
                ('report', models.TextField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prijava',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('akcija', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Akcija')),
                ('korisnik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('photo', models.URLField(default='http://www.aspirehire.co.uk/aspirehire-co-uk/_img/profile.svg')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]