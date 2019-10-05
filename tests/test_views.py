from django.test import TestCase
from django.urls import reverse

from shortener.models import Url


class RedirectViewTestCase(TestCase):
    def setUp(self):
        self.redirect = 'https://pennlabs.org'
        self.url = Url.objects.get_or_create(long_url=self.redirect)

    def test_exists(self):
        response = self.client.get(reverse('shortener:index', args=['fbfed']))
        self.assertRedirects(response, self.redirect, fetch_redirect_response=False)

    def test_no_exists(self):
        response = self.client.get(reverse('shortener:index', args=['abcd']))
        self.assertEqual(response.status_code, 404)
