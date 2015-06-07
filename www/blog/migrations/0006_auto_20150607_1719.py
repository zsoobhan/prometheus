# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogentry_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=4096)),
                ('slug', models.SlugField(max_length=4096)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('blurb', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blogentry',
            name='tag',
            field=models.ManyToManyField(related_name='blog_entry', to='blog.Tag'),
            preserve_default=True,
        ),
    ]
