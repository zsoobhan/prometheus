# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150517_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='date',
            field=models.DateField(help_text=b'The date visible on the post', null=True, blank=True),
            preserve_default=True,
        ),
    ]
