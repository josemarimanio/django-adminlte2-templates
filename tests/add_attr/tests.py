from django.test import Client
from django.test import SimpleTestCase

from adminlte2_templates.core import reverse


class AddAttrTestCase(SimpleTestCase):
    """
    Test cases for 'add_attr' template filter
    """
    URL_PATTERN_INDEX = 'add_attr:index'

    def setUp(self):
        self.client = Client()

    def get_response_index(self):
        return self.client.get(reverse(self.URL_PATTERN_INDEX))

    def test_add_attr(self):
        self.assertContains(self.get_response_index(),
                            '<input type="text" name="name" maxlength="50" readonly="readonly" required id="id_name">',
                            html=True)

    def test_add_attr_html5(self):
        self.assertContains(self.get_response_index(),
                            '<input type="text" name="name" maxlength="50" disabled required id="id_name">', html=True)

    def test_add_attr_multiple(self):
        self.assertContains(self.get_response_index(),
                            '<input type="text" name="name" maxlength="50" readonly="readonly" disabled="disabled" '
                            'required id="id_name">', html=True)
