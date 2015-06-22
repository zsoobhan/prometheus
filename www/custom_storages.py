from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION

    def url(self, name):
        # temporary fix due to a missing / in boto-generated urls
        # http://code.larlet.fr/django-storages/issue/121/s3boto-admin-prefix-issue-with-django-14  # noqa
        url = super(StaticStorage, self).url(name)
        if name.endswith('/') and not url.endswith('/'):
            url += '/'
        return url
