# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150607_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='meta_description',
            field=models.TextField(max_length=1024, blank=True),
            preserve_default=True,
        ),
    ]
