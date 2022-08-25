# -*- coding: utf-8 -*-
import os
import sys

location = lambda *path: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "..", *path
)

DEBUG = TEMPLATE_DEBUG = False

TEST_RUNNER = "django.test.runner.DiscoverRunner"

ATOMIC_REQUESTS = True

LANGUAGE_CODE = "en-gb"

SITE_ID = 1

TIME_ZONE = "Europe/London"
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = location("public/media")
MEDIA_URL = "/media/"
PRIVATE_MEDIA_URL = "/media/private/"

STATIC_ROOT = location("public/static/")

STATIC_URL = "/static/"

ADMIN_MEDIA_PREFIX = "/static/admin/"

# Email Settings
SERVER_EMAIL = "django@zsoobhan.co.uk"
DEFAULT_FROM_EMAIL = "app@zsoobhan.co.uk"
COMMUNICATION_EMAIL = "zsoobhan@gmail.com"

# Additional locations of static files
STATICFILES_DIRS = (location("static/"),)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

ALLOWED_HOSTS = [
    "zsoobhan.co.uk",
    "www.zsoobhan.co.uk",
]

# Use cached template loading by default
TEMPLATE_LOADERS = (
    (
        "django.template.loaders.cached.Loader",
        (
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ),
    ),
)

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    # custom context processors
    "content.context_processors.add_ga_tracking_code",
    "content.context_processors.add_robots_question",
]

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # Custom middleware
    "content.middleware.QuestionMiddleware",
)

ROOT_URLCONF = "urls"

TEMPLATE_DIRS = (location("templates"),)

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "flat",
    "ckeditor",
    "django.contrib.admin",
    "django.contrib.staticfiles",
    "django_extensions",
    "storages",
    "compressor",
    "ckeditor_uploader",
    "s3direct",
    # Prometheus Apps go here
    "content",
    "blog",
]

# Use cached sessions by default
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_COOKIE_HTTPONLY = True

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

COMPRESS_ENABLED = True
COMPRESS_OUTPUT_DIR = "cache"
COMPRESS_CACHE_KEY_FUNCTION = "compressor.cache.socket_cachekey"
COMPRESS_OFFLINE = True

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "127.0.0.1:11211",
    }
}


def create_logging_dict(root):
    """
    Create a logging dict using the passed root for log files

    Note the file handlers don't rotate their files.  This should be handled by
    logrotate (there is a sample conf file in www/deploy/logrotate.d).
    """
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"  # noqa
            },
            "simple": {"format": "%(levelname)s %(message)s"},
        },
        "filters": {
            "require_debug_false": {
                "()": "django.utils.log.RequireDebugFalse",
            },
            "require_debug_true": {
                "()": "django.utils.log.RequireDebugTrue",
            },
        },
        "handlers": {
            "null": {
                "level": "DEBUG",
                "class": "django.utils.log.NullHandler",
            },
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "verbose",
                "filters": ["require_debug_true"],
                "stream": sys.stdout,
            },
            "error_file": {
                "level": "INFO",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": os.path.join(root, "errors.log"),
                "filters": ["require_debug_false"],
                "formatter": "verbose",
            },
            "mail_admins": {
                "level": "ERROR",
                "filters": ["require_debug_false"],
                "class": "django.utils.log.AdminEmailHandler",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["console"],
                "level": "DEBUG",
                "propagate": False,
            },
            # Log errors to console only when DEBUG=True but to both file and
            # admins when DEBUG=False
            "django.request": {
                "handlers": ["console", "error_file", "mail_admins"],
                "level": "ERROR",
                "propagate": False,
            },
            # Enable this logger to see SQL queries
            "django.db.backends": {
                "handlers": ["null"],
                "level": "INFO",
                "propagate": False,
            },
        },
    }


CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
        "uiColor": "#79aec8",
        "toolbarCanCollapse": "true",
    },
}
CKEDITOR_UPLOAD_PATH = "uploads/cke/"
CKEDITOR_IMAGE_BACKEND = "pillow"

# Debug toolbar settings
DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ("127.0.0.1",)
