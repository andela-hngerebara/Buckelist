# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 12:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bucketlistapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('review', models.TextField()),
                ('rating', models.IntegerField()),
                ('buckelist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='bucketlistapi.Bucketlist')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
