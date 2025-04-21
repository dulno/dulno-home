from django.shortcuts import render
from django.http import HttpResponse

def handler404(request, *args, **argv):
  return render(request, 'errors/404.html', {'title': 'Dulno - Page not found',
    'css': ['css/errors/404.css']})