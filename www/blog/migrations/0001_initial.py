# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_published', models.DateTimeField(db_index=True, null=True, blank=True)),
                ('date', models.DateField(help_text=b'The date visible on the post', null=True, blank=True)),
                ('status', models.CharField(default=b'DRAFT', help_text=b'The status of the blog article', max_length=b'16', choices=[(b'PUBLISHED', b'Published'), (b'DRAFT', b'Draft')])),
                ('title', models.CharField(max_length=4096)),
                ('slug', models.SlugField(unique=True, max_length=4096)),
                ('subtitle', models.CharField(max_length=4096, blank=True)),
                ('content', ckeditor.fields.RichTextField(blank=True)),
                ('meta_description', models.TextField(max_length=1024, blank=True)),
            ],
            options={
                'ordering': ['-date_published'],
                'get_latest_by': 'date_published',
                'verbose_name': 'Blog Entry',
                'verbose_name_plural': 'Blog Entries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=4096)),
                ('slug', models.SlugField(unique=True, max_length=4096)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('blurb', ckeditor.fields.RichTextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blogentry',
            name='tags',
            field=models.ManyToManyField(related_name='blog_entries', to='blog.Tag'),
            preserve_default=True,
        ),
    ]
