from django.test import Client
from django.test import TestCase

from adminlte2_templates.core import reverse


class AddActiveTestCase(TestCase):
    """
    Test cases for {% add_active %} template tag

    Testing these cases:

        * Sanity check
        * 'exact_match', 'not_when' params
        * 'pk' arg
    """
    URL_PATTERN_INDEX = 'add_active:index'
    URL_PATTERN_CHILD = 'add_active:child'
    URL_PATTERN_PK = 'add_active:pk'

    def setUp(self):
        self.client = Client()

    def get_response_index(self):
        return self.client.get(reverse(self.URL_PATTERN_INDEX))

    def get_response_child(self):
        return self.client.get(reverse(self.URL_PATTERN_CHILD))

    def get_response_pk(self, pk):
        return self.client.get(reverse(self.URL_PATTERN_PK, args=(pk,)))

    #
    #   Sanity check
    #
    def test_with_active(self):
        self.assertContains(self.get_response_child(), '<p id="with-active"> active </p>', html=True)

    def test_without_active(self):
        self.assertContains(self.get_response_index(), '<p id="without-active"></p>', html=True)

    #
    #   'exact_match' parameter
    #
    def test_exact_match_true(self):
        self.assertContains(self.get_response_child(), '<p id="exact-match-true"></p>', html=True)

    def test_exact_match_false(self):
        self.assertContains(self.get_response_child(), '<p id="exact-match-false"> active </p>', html=True)

    #
    #   'not_when' parameter
    #
    def test_not_when_with_match(self):
        self.assertContains(self.get_response_index(), '<p id="not-when-with-match"></p>', html=True)

    def test_not_when_with_match_multiple(self):
        self.assertContains(self.get_response_index(), '<p id="not-when-with-match-multiple"></p>', html=True)

    def test_not_when_without_match(self):
        self.assertContains(self.get_response_index(), '<p id="not-when-without-match"> active </p>', html=True)

    def test_not_when_without_match_multiple(self):
        self.assertContains(self.get_response_index(), '<p id="not-when-without-match-multiple"> active </p>',
                            html=True)

    #
    #   'pk' arg
    #
    def test_detailview_pk(self):
        self.assertContains(self.get_response_pk(1), '<p id="detailview-pk"> active </p>', html=True)
