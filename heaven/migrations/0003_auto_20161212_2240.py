# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 06:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('heaven', '0002_auto_20161116_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='burial',
            name='DoB',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='burial',
            name='DoD',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Death'),
        ),
        migrations.AlterField(
            model_name='burial',
            name='cemetery_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heaven.Cemetery', verbose_name='Cemetery ID'),
        ),
        migrations.AlterField(
            model_name='burial',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='burial',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='cemetery',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cemetery',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='cemetery',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Cemetery Name'),
        ),
    ]
