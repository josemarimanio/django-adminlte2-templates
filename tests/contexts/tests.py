from django.test import Client
from django.test import SimpleTestCase

from adminlte2_templates.core import reverse


class ContextTestCase(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def context_exists(self, context):
        # Get view from 'layouts' unit test
        response = self.client.get(reverse('layouts:default_boxed'))
        try:
            return response.context[context] is not None
        except KeyError:
            return False

    def test_debug_context(self):
        self.assertTrue(self.context_exists('DEBUG'))

    def test_html_lang_context(self):
        self.assertTrue(self.context_exists('ADMINLTE_HTML_LANG'))

    def test_skin_style_context(self):
        self.assertTrue(self.context_exists('ADMINLTE_SKIN_STYLE'))

    def test_control_style_context(self):
        self.assertTrue(self.context_exists('ADMINLTE_CONTROL_STYLE'))

    def test_use_shim_context(self):
        self.assertTrue(self.context_exists('ADMINLTE_USE_SHIM'))

    def test_use_cdn_context(self):
        self.assertTrue(self.context_exists('ADMINLTE_USE_CDN'))

    def test_use_cdn_context_true(self):
        with self.settings(ADMINLTE_USE_CDN=True):
            self.assertTrue(self.context_exists('ADMINLTE_CDN_ADMINLTE_CSS_CORE'))
            self.assertTrue(self.context_exists('ADMINLTE_CDN_ADMINLTE_CSS_SKIN'))
            self.assertTrue(self.context_exists('ADMINLTE_CDN_ADMINLTE_JS_CORE'))
            self.assertTrue(self.context_exists('ADMINLTE_CDN_BOOTSTRAP_CSS_CORE'))
            self.assertTrue(self.context_exists('ADMINLTE_CDN_BOOTSTRAP_JS_CORE'))
            self.assertTrue(self.context_exists('ADMINLTE_CDN_FONTAWESOME_CSS_CORE'))
            self.assertTrue(self.context_exists('ADMINLTE_CDN_JQUERY_JS_CORE'))

    def test_use_cdn_context_false(self):
        with self.settings(ADMINLTE_USE_CDN=False):
            self.assertFalse(self.context_exists('ADMINLTE_CDN_ADMINLTE_CSS_CORE'))
            self.assertFalse(self.context_exists('ADMINLTE_CDN_ADMINLTE_CSS_SKIN'))
            self.assertFalse(self.context_exists('ADMINLTE_CDN_ADMINLTE_JS_CORE'))
            self.assertFalse(self.context_exists('ADMINLTE_CDN_BOOTSTRAP_CSS_CORE'))
            self.assertFalse(self.context_exists('ADMINLTE_CDN_BOOTSTRAP_JS_CORE'))
            self.assertFalse(self.context_exists('ADMINLTE_CDN_FONTAWESOME_CSS_CORE'))
            self.assertFalse(self.context_exists('ADMINLTE_CDN_JQUERY_JS_CORE'))

    def test_use_cdn_and_use_shim_context_true(self):
        with self.settings(ADMINLTE_USE_CDN=True, ADMINLTE_USE_SHIM=True):
            self.assertTrue(self.context_exists('ADMINLTE_CDN_HTML5SHIV_CORE_JS'))
            self.assertTrue(self.context_exists('ADMINLTE_CDN_RESPOND_CORE_JS'))

    def test_use_cdn_and_use_shim_context_false(self):
        with self.settings(ADMINLTE_USE_CDN=True, ADMINLTE_USE_SHIM=False):
            self.assertFalse(self.context_exists('ADMINLTE_CDN_HTML5SHIV_CORE_JS'))
            self.assertFalse(self.context_exists('ADMINLTE_CDN_RESPOND_CORE_JS'))
