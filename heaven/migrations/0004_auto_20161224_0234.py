# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-24 10:34
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heaven', '0003_auto_20161212_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='cemetery',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=Decimal('0.000000'), max_digits=8),
        ),
        migrations.AddField(
            model_name='cemetery',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=Decimal('0.000000'), max_digits=9),
        ),
    ]
