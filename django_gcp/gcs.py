"""
GoogleCloudStorage extensions suitable for handing Django's
Static and Media files.

Requires following settings:
MEDIA_URL, GS_MEDIA_BUCKET_NAME
STATIC_URL, GS_STATIC_BUCKET_NAME

In addition to
https://django-storages.readthedocs.io/en/latest/backends/gcloud.html
"""
from django.conf import settings
from storages.backends.gcloud import GoogleCloudStorage
from urllib.parse import urljoin


class GoogleCloudMediaStorage(GoogleCloudStorage):
    """GoogleCloudStorage suitable for Django's Media files."""

    def __init__(self, *args, **kwargs):
        kwargs['bucket_name'] = settings.GS_MEDIA_BUCKET_NAME
        super(GoogleCloudMediaStorage, self).__init__(*args, **kwargs)


class GoogleCloudStaticStorage(GoogleCloudStorage):
    """GoogleCloudStorage suitable for Django's Static files"""

    def __init__(self, *args, **kwargs):
        kwargs['bucket_name'] = settings.GS_STATIC_BUCKET_NAME
        kwargs['default_acl'] = 'publicRead'
        super(GoogleCloudStaticStorage, self).__init__(*args, **kwargs)