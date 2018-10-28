import hashlib

from django.db import models
from django.conf import settings


class Url(models.Model):
    long_url = models.TextField()
    short_id = models.TextField()

    @property
    def shortened(self):
        return '%s/s/%s' % (settings.BASE_URL, self.short_id)


def shorten(long_url):
    hashed = hashlib.sha3_256(long_url.encode('utf-8')).hexdigest()
    length = 5

    while Url.objects.filter(short_id=hashed[:length]).exists():
        length += 1

    url = Url(long_url=long_url, short_id=hashed[:length])
    url.save()
    return url.short_id
