from django.db import models


PUBLISHED = 'PUBLISHED'
DRAFT = 'DRAFT'
STATUS_CHOICES = [
    (PUBLISHED, 'Published'),
    (DRAFT, 'Draft')]


# FIXME: think about indexing more fields
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

    def __unicode__(self):
        return u'<Slug:%s -- Pub:%s>' % (self.slug, self.date_created.date())

    class Meta:
        get_latest_by = 'date_published'
        ordering = ['-date_published']
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
