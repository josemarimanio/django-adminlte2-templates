from django.test import Client
from django.test import TestCase

from django.contrib.sites.models import Site

try:
    # Supports >=Django 2.0
    from django.shortcuts import reverse
except ImportError:
    # Supports <=Django 1.1
    from django.core.urlresolvers import reverse


class AddActiveTestCase(TestCase):
    """
    Test cases for {% add_active %} template tag
    """

    def setUp(self):
        self.client = Client()

        self.response_index = self.client.get(reverse('add_active:index'))  # /add_active/
        self.response_child = self.client.get(reverse('add_active:child'))  # /add_active/child/
        self.response_pk = self.client.get(reverse('add_active:pk', args=(1,)))  # /add_active/<pk>/

    def test_with_active(self):
        self.assertContains(self.response_child, '<p id="with-active"> active </p>')

    def test_without_active(self):
        self.assertContains(self.response_index, '<p id="without-active"></p>')

    def test_exact_match_true(self):
        self.assertContains(self.response_child, '<p id="exact-match-true"></p>')

    def test_exact_match_false(self):
        self.assertContains(self.response_child, '<p id="exact-match-false"> active </p>')

    def test_not_when_with_match(self):
        self.assertContains(self.response_index, '<p id="not-when-with-match"></p>')

    def test_not_when_with_match_multiple_parameters(self):
        self.assertContains(self.response_index, '<p id="not-when-with-match-multiple"></p>')

    def test_not_when_without_match(self):
        self.assertContains(self.response_index, '<p id="not-when-without-match"> active </p>')

    def test_detailview_pk(self):
        self.assertContains(self.response_pk, '<p id="detailview-pk"> active </p>')
