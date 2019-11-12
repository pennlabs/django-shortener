from django.urls import path

from shortener.views import RedirectView


app_name = "shortener"

urlpatterns = [path("<slug:short>/", RedirectView.as_view(), name="index")]
