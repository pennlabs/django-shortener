# Django Shortener

[![CircleCI](https://circleci.com/gh/pennlabs/django-shortener.svg?style=shield)](https://circleci.com/gh/pennlabs/django-shortener)
[![Coverage Status](https://codecov.io/gh/pennlabs/django-shortener/branch/master/graph/badge.svg)](https://codecov.io/gh/pennlabs/django-shortener)
[![PyPi Package](https://img.shields.io/pypi/v/shortener.svg)](https://pypi.org/project/shortener/)

Basic URL shortener as a Django app.

## Requirements

* Python 3.6+
* Django 2.2+

## Installation

Install with pip `pip install shortener`

Add `shortener` to `INSTALLED_APPS`

```python
INSTALLED_APPS = (
    ...
    'shortener.apps.ShortenerConfig',
    ...
)
```

Add the following to `urls.py`

```python
urlpatterns = [
    ...
    path('s/', include('shortener.urls', namespace='shortener')),
    ...
]
```

This will shorten URLs to `example.com/s/<slug>`

Run migrations `./manage.py migrate`

## Documentation

Shortened URLs can be created using the django admin site or by calling `shortener.models.Url.get_or_create()` with the URL you want to shorten.

## Changelog

See [CHANGELOG.md](https://github.com/pennlabs/django-runtime-options/blob/master/CHANGELOG.md)

## License

See [LICENSE](https://github.com/pennlabs/django-runtime-options/blob/master/LICENSE)
