from ckeditor.fields import RichTextField
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.db import models


PUBLISHED = 'PUBLISHED'
DRAFT = 'DRAFT'
STATUS_CHOICES = [
    (PUBLISHED, 'Published'),
    (DRAFT, 'Draft')]


class Tag(models.Model):
    title = models.CharField(max_length=4096)
    slug = models.SlugField(max_length=4096, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    blurb = RichTextField(blank=True)

    def __unicode__(self):
        return u'{slug}'.format(slug=self.slug)


class BlogEntry(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(null=True, blank=True, db_index=True)
    date = models.DateField(
        null=True,
        blank=True,
        help_text='The date visible on the post')
    status = models.CharField(
        max_length='16',
        help_text='The status of the blog article',
        choices=STATUS_CHOICES,
        default=DRAFT)
    title = models.CharField(max_length=4096)
    slug = models.SlugField(max_length=4096, unique=True)
    subtitle = models.CharField(blank=True, max_length=4096)
    content = RichTextField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='blog_entries')
    meta_description = models.TextField(blank=True, max_length=1024)
    icon = models.CharField(
        max_length=64,
        help_text='The font awesome icon to be displayed',
        default='fa-align-right')

    class Meta:
        get_latest_by = 'date_published'
        ordering = ['-date_published']
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"

    def __unicode__(self):
        return u'slug'.format(slug=self.slug)

    @property
    def is_active(self):
        published_now = False

        conditions = [self.status == PUBLISHED]
        if self.date_published:
            published_now = self.date_published <= timezone.now()
        conditions.append(published_now)
        return all(conditions)

    @property
    def get_ga_label(self):
        return '{slug}-{id}'.format(slug=self.slug[:10], id=self.id)

    def get_absolute_url(self):
        return reverse(
            'blog:blog-entry-detail-view', kwargs={'slug': self.slug})
