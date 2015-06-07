# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150607_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
    ]
