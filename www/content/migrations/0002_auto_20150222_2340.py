# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communication',
            name='message',
            field=models.TextField(help_text=b'Your message goes here.', max_length=4096),
            preserve_default=True,
        ),
    ]
