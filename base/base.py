from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
import os
from django.conf import settings

def favicon(request):
  filepath = os.path.join(settings.BASE_DIR + '/static/img/', 'icon-dark.ico')
  return FileResponse(open(filepath, 'rb'), content_type='image/x-icon')

def close(request):
  return render(request, 'close/close.html')