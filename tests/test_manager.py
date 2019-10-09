from unittest.mock import patch

from django.test import TestCase

from shortener.models import Url


class UrlTestCase(TestCase):
    def setUp(self):
        self.redirect = 'https://pennlabs.org'

    def test_exists(self):
        url, created1 = Url.objects.get_or_create(long_url=self.redirect)
        self.assertEqual(len(Url.objects.all()), 1)
        self.assertTrue(created1)
        _, created2 = Url.objects.get_or_create(long_url=self.redirect)
        self.assertFalse(created2)
        self.assertEqual(len(Url.objects.all()), 1)
        self.assertEqual(Url.objects.all()[0], url)

    def test_no_exists(self):
        self.assertEqual(len(Url.objects.all()), 0)
        url, created = Url.objects.get_or_create(long_url=self.redirect)
        self.assertTrue(created)
        self.assertEqual(len(Url.objects.all()), 1)
        self.assertEqual(Url.objects.all()[0], url)

    @patch('shortener.manager.hashlib')
    def test_collision(self, mock_hash):
        try:
            mock_hash.sha3_256.return_value.hexdigest.return_value = 'abcdef'
        except AttributeError:
            mock_hash.sha256.return_value.hexdigest.return_value = 'abcdef'
        url1, created1 = Url.objects.get_or_create(long_url='url1')
        url2, created2 = Url.objects.get_or_create(long_url='url2')
        self.assertEqual(url1.short_id, 'abcde')
        self.assertTrue(created1)
        self.assertEqual(url2.short_id, 'abcdef')
        self.assertTrue(created2)
