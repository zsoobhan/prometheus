# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_blogentry_meta_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogentry',
            name='date_created',
        ),
    ]
