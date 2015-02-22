# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150222_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='slug',
            field=models.SlugField(max_length=4096),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogentry',
            name='subtitle',
            field=models.CharField(max_length=4096, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogentry',
            name='title',
            field=models.CharField(max_length=4096),
            preserve_default=True,
        ),
    ]
