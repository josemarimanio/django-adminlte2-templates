from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.template.exceptions import TemplateSyntaxError
from django.test import Client
from django.test import TestCase
from django.test import SimpleTestCase

from adminlte2_templates import constants as const
from adminlte2_templates.core import reverse
