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
async def product(request):
  return render(request, 'product.html', {'title': gettext("home.product.title"),
    'css': ['css/base/home-header.css', 'css/base/home-language.css',
      'css/base/home-footer.css', 'css/home/product.css']})

@home_page
async def solution(request):
  return render(request, 'solution.html', {'title': gettext("home.solution.title"),
    'css': ['css/base/home-header.css', 'css/base/home-language.css',
      'css/base/home-footer.css', 'css/home/solution.css']})

@home_page
async def download(request):
  return render(request, 'download.html', {'title': gettext("home.download.title"),
    'css': ['css/base/home-header.css', 'css/base/home-language.css',
      'css/base/home-footer.css', 'css/home/download.css']})

@home_page
async def pricing(request):
  return render(request, 'pricing.html', {'title': gettext("home.pricing.title"),
    'css': ['css/base/home-header.css', 'css/base/home-language.css',
      'css/base/home-footer.css', 'css/home/pricing.css', 'css/base/pricing-content.css']})

@home_page
async def question(request):
  return render(request, 'question.html', {'title': gettext("home.question.title"),
    'css': ['css/base/home-header.css', 'css/base/home-language.css',
      'css/base/home-footer.css', 'css/home/question.css']})

@home_page
async def sale(request):
  return render(request, 'sale.html', {'title': gettext("home.sale.title"),
    'css': ['css/base/home-header.css', 'css/base/home-language.css',
      'css/base/home-footer.css', 'css/home/sale.css']})

@home_page
async def imprint(request):
  return render(request, 'imprint.html', {'title': gettext("home.imprint.title"),
    'css': ['css/base/home-header.css', 'css/base/home-language.css',
      'css/base/home-footer.css', 'css/home/imprint.css']})

@home_page
async def privacyPolicy(request):
  return render(request, 'privacy-policy.html', {'title': gettext("home.privacy.policy.title"),
    'css': ['css/base/home-header.css', 'css/base/home-language.css',
      'css/base/home-footer.css', 'css/home/privacy-policy.css']})

@home_page
async def termsOfService(request):
  return render(request, 'terms-of-service.html', {'title': gettext("home.terms.of.service.title"),
    'css': ['css/base/home-header.css', 'css/base/home-language.css',
      'css/base/home-footer.css', 'css/home/terms-of-service.css']})