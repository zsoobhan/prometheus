# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_blogentry_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 7, 21, 39, 19, 414936, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
