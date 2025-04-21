from django.urls import path, include
from . import base

urlpatterns = [
  path('favicon.ico', base.favicon),
  path('close/', base.close),
]