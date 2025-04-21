from django.urls import path, include
from django.conf.urls import handler404
from errors import errors
from app.settings import ENVIRONMENT
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

handler404 = errors.handler404

urlpatterns = [
  path('', include('base.urls')),
  path('', include('home.urls')),
]

if ENVIRONMENT == 'LOCAL':
  urlpatterns += staticfiles_urlpatterns()