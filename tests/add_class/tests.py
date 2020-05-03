from django.test import Client
from django.test import SimpleTestCase

from adminlte2_templates.core import reverse


class AddClassTestCase(SimpleTestCase):
    """
    Test cases for 'add_class' template filter
    """
    URL_PATTERN_INDEX = 'add_class:index'

    def setUp(self):
        self.client = Client()

    def get_response_index(self):
        return self.client.get(reverse(self.URL_PATTERN_INDEX))

    def test_add_class(self):
        self.assertContains(self.get_response_index(), 'add-class')

    def test_add_class_multiple(self):
        self.assertContains(self.get_response_index(), 'add-class-1 add-class-2')
