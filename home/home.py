from functools import wraps
from functools import partial
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import translation
from django.utils.translation import gettext

def home_page(function):
  @wraps(function)
  async def home_page(request, *args, **kwargs):
    applyLanguage(request)
    return await function(request, *args, **kwargs)
  return home_page

def applyLanguage(request):
  language = request.COOKIES.get("dulno-home-language")
  if (language is None):
    translation.activate("en")
  translation.activate(language)

@home_page
async def home(request):
  return render(request, 'home.html', {'title': gettext("home.title"),
    'css': ['css/base/home-header.css', 'css/base/home-language.css',
      'css/base/home-footer.css', 'css/home/home.css', 'css/base/pricing-content.css'],
    'isNavbarStatic': True})

@home_page
async def app(request):
  return render(request, 'app.html', {'title': '', 'css': []})

@home_page
async def imprint(request):
  return render(request, 'imprint.html', {'title': gettext("imprint.title"),
    'css': ['css/base/home-header.css', 'css/base/home-language.css',
      'css/base/home-footer.css', 'css/home/imprint.css']})

@home_page
async def privacyPolicy(request):
  return render(request, 'privacy-policy.html', {'title': gettext("privacy.policy.title"),
    'css': ['css/base/home-header.css', 'css/base/home-language.css',
      'css/base/home-footer.css', 'css/home/privacy-policy.css']})

@home_page
async def termsOfService(request):
  return render(request, 'terms-of-service.html', {'title': gettext("terms.of.service.title"),
    'css': ['css/base/home-header.css', 'css/base/home-language.css',
      'css/base/home-footer.css', 'css/home/terms-of-service.css']})