import logging
import os
import asyncio
import requests
import json
import jwt
from django.conf import settings

class ExceptionHandler(logging.Handler):
  def __init__(self):
    super().__init__()

  def emit(self, record):
    try:
      if record.exc_info:
        trace = self.format(record)
        exception_type = record.exc_info[0]
        exception_message = str(record.exc_info[1])
        full_exception_type = f"{exception_type.__module__}.{exception_type.__name__}: {exception_message}"
        body = {
          "reportKey": os.getenv('ERROR_REPORT_KEY', '').replace("\n", ""),
          "title": full_exception_type,
          "trace": trace,
          "origin": "Web",
          "pod": os.getenv('POD_NAME', ''),
          "podControllerName": os.getenv('CONTROLLER_NAME', ''),
          "podControllerType": os.getenv('CONTROLLER_TYPE', ''),
          "node": os.getenv('NODE_NAME', ''),
        }
        requests.post("http://10.96.0.9/v1/cluster/error/report/", json=body)
    except Exception as exception:
      print(f"Exception in ExceptionHandler: {exception}")