from django.urls import path, include
from . import home

urlpatterns = [
  path('', home.home),
  path('home/', home.home),
  path('app/', home.app),
  path('portal/', home.portal),
  path('question/', home.question),
  path('imprint/', home.imprint),
  path('privacy-policy/', home.privacyPolicy),
  path('terms-of-service/', home.termsOfService),
]