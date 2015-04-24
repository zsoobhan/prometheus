import datetime
from django.db import models


PUBLISHED = 'PUBLISHED'
DRAFT = 'DRAFT'
STATUS_CHOICES = [
    (PUBLISHED, 'Published'),
    (DRAFT, 'Draft')]


# FIXME: think about indexing more fields
#        add an indexed published field that is updated on save?
class BlogEntry(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateField(null=True, blank=True, db_index=True)
    status = models.CharField(
        max_length='16',
        help_text='The status of the blog article',
        choices=STATUS_CHOICES,
        default=DRAFT)
    title = models.CharField(max_length=4096)
    slug = models.SlugField(max_length=4096)
    subtitle = models.CharField(blank=True, max_length=4096)
    content = models.TextField(blank=True)

    class Meta:
        get_latest_by = 'date_published'
        ordering = ['-date_published']
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"

    def __unicode__(self):
        return u'<BlogEntry:%s -- %s>' % (self.slug, self.date_created.date())

    @property
    def is_published(self):
        conditions = [
            self.date_published >= datetime.date.today(),
            self.status == PUBLISHED]
        return all(conditions)
