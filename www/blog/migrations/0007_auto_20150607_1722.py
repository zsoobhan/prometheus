# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150607_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='slug',
            field=models.SlugField(unique=True, max_length=4096),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(unique=True, max_length=4096),
            preserve_default=True,
        ),
    ]
