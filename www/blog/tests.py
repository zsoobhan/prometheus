import factory
import datetime

from django.utils import timezone
from django.test import TestCase

from . import models


class BlogEntryTests(TestCase):

    def setUp(self):
        self.blog_entry = BlogEntryFactory.create()

    def test_blog_is_active_published_past(self):
        self.blog_entry.date_published = past()
        self.blog_entry.save()

        self.assertTrue(self.blog_entry.is_active)

    def test_blog_is_inactive_published_future(self):
        self.blog_entry.date_published = future()
        self.blog_entry.save()

        self.assertFalse(self.blog_entry.is_active)

    def test_blog_is_inactive_published_not_published(self):
        self.blog_entry.date_published = past()
        self.blog_entry.status = models.DRAFT
        self.blog_entry.save()

        self.assertFalse(self.blog_entry.is_active)

    def test_blog_is_inactive_published_no_date_published(self):
        self.blog_entry.date_published = None
        self.blog_entry.status = models.PUBLISHED
        self.blog_entry.save()

        self.assertFalse(self.blog_entry.is_active)


# Test Utils
class BlogEntryFactory(factory.django.DjangoModelFactory):
    status = models.PUBLISHED
    title = 'This is a test title'
    subtitle = 'This is a test subtitle'
    content = 'The quick brown fox jumps over the lazy dog. '*10
    slug = factory.Sequence(lambda n: "slug-%03d" % n)

    class Meta:
        model = models.BlogEntry


def past():
    return timezone.now() - datetime.timedelta(days=1)


def future():
    return timezone.now() + datetime.timedelta(days=1)
