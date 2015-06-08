from s3direct.fields import S3DirectField
from django.db.models.signals import post_save
from django.db import models

from . import signals


class Communication(models.Model):

    email = models.EmailField(max_length=254)
    message = models.TextField(
        help_text="Your message goes here.",
        max_length=4096)
    name = models.CharField(
        max_length=64,
        help_text="Your name goes here.")
    phone_number = models.CharField(
        max_length=16,
        blank=True,
        help_text='Your phone number goes here.')
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'Name:%s -- Date:%s' % (self.name, self.date_created.date())


class Upload(models.Model):
    name = models.CharField(max_length=64)
    date_created = models.DateTimeField(auto_now_add=True)
    upload_file = S3DirectField(dest='uploads')

    def __unicode__(self):
        return u'{name}'.format(name=self.name)


post_save.connect(signals.notify, sender=Communication)
