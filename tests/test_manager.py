from unittest.mock import patch

from django.test import TestCase

from shortener.models import Url


class UrlTestCase(TestCase):
    def setUp(self):
        self.redirect = 'https://pennlabs.org'

    def test_exists(self):
        url = Url.objects.get_or_create(long_url=self.redirect)
        self.assertEqual(len(Url.objects.all()), 1)
        Url.objects.get_or_create(long_url=self.redirect)
        self.assertEqual(len(Url.objects.all()), 1)
        self.assertEqual(Url.objects.all()[0], url)

    def test_no_exists(self):
        self.assertEqual(len(Url.objects.all()), 0)
        url = Url.objects.get_or_create(long_url=self.redirect)
        self.assertEqual(len(Url.objects.all()), 1)
        self.assertEqual(Url.objects.all()[0], url)

    @patch('shortener.manager.hashlib.sha3_256')
    def test_collision(self, mock_hash):
        mock_hash.return_value.hexdigest.return_value = 'abcdef'
        url1 = Url.objects.get_or_create(long_url='url1')
        url2 = Url.objects.get_or_create(long_url='url2')
        self.assertEqual(url1.short_id, 'abcde')
        self.assertEqual(url2.short_id, 'abcdef')
