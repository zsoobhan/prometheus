from django.db.models.signals import post_save
from django.db import models

from . import signals


class Communication(models.Model):

    email = models.EmailField(max_length=254)
    message = models.TextField(
        help_text="Your message goes here.")
    name = models.CharField(
        max_length=64,
        help_text="Your name goes here.")
    phone_number = models.CharField(
        max_length=16,
        blank=True,
        help_text='Your phone number goes here.')
    date_created = models.DateTimeField(auto_now_add=True)


post_save.connect(signals.notify_admin, sender=Communication)
