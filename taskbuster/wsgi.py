"""
WSGI config for taskbuster project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.core.exceptions import ImproperlyConfigured

# Handling Key Import Errors
def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

DJANGO_SETTINGS_MODULE = get_env_variable('DJANGO_SETTINGS_MODULE')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskbuster.settings")

application = get_wsgi_application()
