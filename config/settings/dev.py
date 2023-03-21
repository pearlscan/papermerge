import logging

from .base import *  # noqa

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DEBUG = True

# INSTALLED_APPS.extend(
#     ['django_extensions']
# )

INTERNAL_IPS = ['127.0.0.1', ]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{levelname} {message}',
            'style': '{'
        },
        'verbose': {
            'format': '%(levelname)-8s | %(module)-16s | %(message)s',
        }
    },
    'handlers': {
        'papermerge': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'root': {
            'handlers': ['papermerge'],
            'level': 'DEBUG'
        },
        'papermerge.core.lib.pdfinfo': {
            'handlers': ['papermerge'],
            'level': 'DEBUG'
        },
        'papermerge.core.importers': {
            'handlers': ['papermerge'],
            'level': 'DEBUG'
        },
        'papermerge.core.import_pipeline': {
            'handlers': ['papermerge'],
            'level': 'DEBUG'
        },
        'papermerge.core.views.documents': {
            'handlers': ['papermerge'],
            'level': 'DEBUG'
        },
        'papermerge.core.ocr.page': {
            'handlers': ['papermerge'],
            'level': 'DEBUG'
        },
        'papermerge.core.tasks': {
            'handlers': ['papermerge'],
            'level': 'DEBUG'
        }
    },
}

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {}
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
