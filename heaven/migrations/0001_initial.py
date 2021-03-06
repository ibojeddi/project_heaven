# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 07:14
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
            name='Burial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('DoB', models.DateField(blank=True, null=True)),
                ('DoD', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')], max_length=1)),
                ('date_created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Cemetery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=5)),
                ('date_created', models.DateTimeField(editable=False)),
                ('date_modified', models.DateTimeField()),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='burial',
            name='cemetery_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heaven.Cemetery'),
        ),
        migrations.AddField(
            model_name='burial',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
