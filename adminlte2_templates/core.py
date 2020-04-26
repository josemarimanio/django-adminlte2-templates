from django.conf import settings

from adminlte2_templates import constants

try:
    # Python 3
    from urllib.parse import urlencode
except ImportError:
    # Python 2.7
    from urllib import urlencode

try:
    # Supports >=Django 2.0
    from django.shortcuts import reverse
except ImportError:
    # Supports <=Django 1.1
    from django.core.urlresolvers import reverse


def get_settings(variable, django_setting=None):
    """
        Get the settings variable from Django ``settings``. If no settings variable
        is found, get the default value from the adminlte2_templates ``constants`` module.

        :param variable: Settings variable name
        :type variable: str

        :param django_setting: Django settings variable to look for before trying to get ``variable``
        :type django_setting: str, optional

        :return: Settings value
    """
    return getattr(settings, django_setting if django_setting else variable, getattr(constants, variable, None))
