# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150607_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogentry',
            name='tag',
        ),
        migrations.AddField(
            model_name='blogentry',
            name='tags',
            field=models.ManyToManyField(related_name='blog_entries', to='blog.Tag'),
            preserve_default=True,
        ),
    ]
