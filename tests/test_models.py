from django.test import TestCase

from shortener.models import Url


class UrlTestCase(TestCase):
    def setUp(self):
        self.url, _ = Url.objects.get_or_create(long_url='https://pennlabs.org')

    def test_str(self):
        self.assertEqual(str(self.url), '{} -- {}'.format(self.url.long_url, self.url.short_id))
