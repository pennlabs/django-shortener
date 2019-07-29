from django.shortcuts import get_object_or_404, redirect
from shortener.models import Url


def index(request, short):
    url = get_object_or_404(Url, short_id=short)
    return redirect(url.long_url)
