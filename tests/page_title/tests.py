from django.contrib.sites.models import Site
from django.test import Client
from django.test import TestCase

from adminlte2_templates.core import reverse


class PageTitleTestCase(TestCase):
    """
    Test cases for {% page_title %} template tag

    Testing these cases:

        * Sanity check
        * 'ADMINLTE_TITLE_SITE', 'ADMINLTE_TITLE_DIVIDER', 'ADMINLTE_TITLE_FORMAT',
            'ADMINLTE_TITLE_FORMAT_PAGINATION' settings
        * 'page_name' param View context override
        * Django 'sites' support
        * ListView support
    """
    URL_PATTERN_INDEX = 'page_title:index'
    URL_PATTERN_LIST = 'page_title:list'
    URL_PATTERN_OVERRIDE = 'page_title:override'

    def setUp(self):
        self.client = Client()

    def add_sites(self):
        for n in range(2):
            Site.objects.create(name=str(n), domain=str(n))

    def add_working_site(self):
        Site.objects.create(domain='testserver', name='testserver')

    def get_response_index(self):
        return self.client.get(reverse(self.URL_PATTERN_INDEX))

    def get_response_list(self, page):
        return self.client.get(reverse(self.URL_PATTERN_LIST) + '?page=' + str(page))

    def get_response_override_page_name(self):
        return self.client.get(reverse(self.URL_PATTERN_OVERRIDE))

    #
    #   Sanity check
    #
    def test_response(self):
        return self.assertContains(self.get_response_index(), 'AdminLTE | Title')

    #
    #   Settings
    #
    def test_settings_site_name(self):
        with self.settings(ADMINLTE_TITLE_SITE='Testing'):
            return self.assertContains(self.get_response_index(), 'Testing | Title')

    def test_settings_divider(self):
        with self.settings(ADMINLTE_TITLE_DIVIDER='@'):
            return self.assertContains(self.get_response_index(), 'AdminLTE @ Title')

    def test_settings_format(self):
        with self.settings(ADMINLTE_TITLE_FORMAT='{site} {divider} {page}'):
            return self.assertContains(self.get_response_index(), 'AdminLTE | Title')

    def test_settings_format_pagination(self):
        with self.settings(ADMINLTE_TITLE_FORMAT_PAGINATION='{site} {divider} {page} ({curr_no} of {last_no})'):
            return self.assertContains(self.get_response_list(1), 'AdminLTE | Title (1 of 1)')

    #
    #   Override page name through View context
    #
    def test_override_context_page_name(self):
        return self.assertContains(self.get_response_override_page_name(), 'AdminLTE | Override')

    #
    #   Django 'sites' support
    #
    def test_sites_site_id(self):
        with self.settings(SITE_ID=1):
            return self.assertContains(self.get_response_index(), 'example.com | Title')

    def test_sites_current_site(self):
        self.add_working_site()
        return self.assertContains(self.get_response_index(), 'testserver | Title')

    def test_sites_failsafe_invalid_site_id(self):
        with self.settings(SITE_ID=2):
            return self.assertContains(self.get_response_index(), 'AdminLTE | Title')

    #
    #   ListView support
    #
    def test_listview_page_1(self):
        self.add_sites()
        return self.assertContains(self.get_response_list(1), 'AdminLTE | Title (1 of 3)')

    def test_listview_page_1_no_add(self):
        return self.assertContains(self.get_response_list(1), 'AdminLTE | Title (1 of 1)')

    def test_listview_page_2(self):
        self.add_sites()
        return self.assertContains(self.get_response_list(2), 'AdminLTE | Title (2 of 3)')

    def test_listview_page_last(self):
        self.add_sites()
        return self.assertContains(self.get_response_list('last'), 'AdminLTE | Title (3 of 3)')
