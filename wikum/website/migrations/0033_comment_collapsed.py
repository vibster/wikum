# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-04 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0032_article_highlight_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='collapsed',
            field=models.BooleanField(default=False),
        ),
    ]
