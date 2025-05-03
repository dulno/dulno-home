from app.settings import ENVIRONMENT

def domain(request):
  if ENVIRONMENT == 'PRODUCTION':
    domain = 'dulno.com'
    base_url = 'https://dulno.com'
    request_prefix = 'https://api.dulno.com/v1'
    public_endpoint = 'https://api.dulno.com'
  elif ENVIRONMENT == 'STAGING':
    domain = 'dulno.dev'
    base_url = 'https://dulno.dev'
    request_prefix = 'https://api.dulno.dev/v1'
    public_endpoint = 'https://pub.dulno.dev'
  elif ENVIRONMENT == 'LOCAL':
    domain = 'dulno.dev'
    base_url = 'https://dulno.dev'
    request_prefix = 'http://10.96.0.4/v1'
    public_endpoint = 'https://pub.dulno.dev'
  return {
    'domain': domain,
    'base_url': base_url,
    'request_prefix': request_prefix,
    'public_endpoint': public_endpoint
  }