from django.urls import path, include
from . import home

urlpatterns = [
  path('', home.home),
  path('home/', home.home),
  path('download/', home.download),
  path('pricing/', home.pricing),
  path('question/', home.question),
  path('sale/', home.sale),
  path('imprint/', home.imprint),
  path('privacy-policy/', home.privacyPolicy),
  path('terms-of-service/', home.termsOfService),
]