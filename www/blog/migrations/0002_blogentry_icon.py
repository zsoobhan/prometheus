# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='icon',
            field=models.CharField(default=b'fa-align-right', help_text=b'The font awesome icon to be displayed', max_length=64),
            preserve_default=True,
        ),
    ]
