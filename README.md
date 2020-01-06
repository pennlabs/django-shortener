# shortener

[![CircleCI](https://circleci.com/gh/pennlabs/shortener.svg?style=shield)](https://circleci.com/gh/pennlabs/shortener)
[![Coverage Status](https://codecov.io/gh/pennlabs/shortener/branch/master/graph/badge.svg)](https://codecov.io/gh/pennlabs/shortener)
[![PyPi Package](https://img.shields.io/pypi/v/shortener.svg)](https://pypi.org/project/shortener/)

Basic URL shortener as a Django app.

To use:

1. Install using pip `pip install shortener`
2. Include `shortener.apps.ShortenerConfig` to `INSTALLED_APPS` in your project's `settings.py`
3. Add the shortener to `urls.py`.
    - Example: `path('s/', include('shortener.urls', namespace='shortener'))` will shorten URLs to `https://example.com/s/<ID>`.
4. `python manage.py migrate`
5. Either add in URL shortcuts manually through Admin, or add some hook in your project to call `shortener.objects.get_or_create`.
The function takes in a long URL and returns a `Url` object which contains the full shortened url as `Url.shortened`, and the slug in `Url.short_id`.
