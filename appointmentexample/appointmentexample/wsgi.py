"""
WSGI config for appointmentexample project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "appointmentexample.settings")
try:
    application = get_wsgi_application()
except:
    import sys
    print(sys.path,sys.stderr)
    raise
