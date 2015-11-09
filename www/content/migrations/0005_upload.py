# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_delete_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('upload_file', s3direct.fields.S3DirectField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
