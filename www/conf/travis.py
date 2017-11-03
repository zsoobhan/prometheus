from conf.default import *  # noqa

DEBUG = TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'travisci',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
ADMINS = (('Ziyad Soobhan', 'zsoobhan@gmail.com'), )

SECRET_KEY = 'thisisateststringandisnotusedinproduction'
GA_TRACKING_CODE = 'XXXXX-XXXX'
