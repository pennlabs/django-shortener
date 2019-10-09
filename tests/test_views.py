import hashlib

from django.test import TestCase
from django.urls import reverse

from shortener.models import Url


class RedirectViewTestCase(TestCase):
    def setUp(self):
        self.redirect = 'https://pennlabs.org'
        self.url, _ = Url.objects.get_or_create(long_url=self.redirect)

    def test_exists(self):
        try:
            hashed = hashlib.sha3_256(self.redirect.encode('utf-8')).hexdigest()
        except AttributeError:
            hashed = hashlib.sha256(self.redirect.encode('utf-8')).hexdigest()
        response = self.client.get(reverse('shortener:index', args=[hashed[:5]]))
        self.assertRedirects(response, self.redirect, fetch_redirect_response=False)

    def test_no_exists(self):
        response = self.client.get(reverse('shortener:index', args=['abcd']))
        self.assertEqual(response.status_code, 404)
