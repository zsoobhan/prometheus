from django.template import loader
from django.core.mail import send_mail

from django.conf import settings


def notify(sender, instance, created, *args, **kwargs):
    body = loader.render_to_string(
        'email/communication_alert.html', {'object': instance})

    send_mail(subject='New Communication',
              message=body,
              from_email=settings.DEFAULT_FROM_EMAIL,
              recipient_list=[settings.COMMUNICATION_EMAIL])
