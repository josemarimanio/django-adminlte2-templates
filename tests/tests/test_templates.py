from tests.imports import *


class TemplateTestCase(SimpleTestCase):

    def setUp(self):
        self.client = Client()

    #
    #   Default
    #
    def test_default_boxed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:default_boxed')),
            const.LAYOUT_DEFAULT_BOXED)

    def test_default_collapsed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:default_collapsed')),
            const.LAYOUT_DEFAULT_COLLAPSED)

    def test_default_fixed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:default_fixed')),
            const.LAYOUT_DEFAULT_FIXED)

    def test_default_login(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:default_login')),
            const.LAYOUT_DEFAULT_LOGIN)

    def test_default_register(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:default_register')),
            const.LAYOUT_DEFAULT_REGISTER)

    def test_default_top_nav(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:default_top_nav')),
            const.LAYOUT_DEFAULT_TOP_NAV)

    #
    #   Barebones
    #
    def test_barebones_boxed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:barebones_boxed')),
            const.LAYOUT_BAREBONES_BOXED)

    def test_barebones_collapsed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:barebones_collapsed')),
            const.LAYOUT_BAREBONES_COLLAPSED)

    def test_barebones_fixed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:barebones_fixed')),
            const.LAYOUT_BAREBONES_FIXED)

    def test_barebones_top_nav(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:barebones_top_nav')),
            const.LAYOUT_BAREBONES_TOP_NAV)

    #
    #   No Breadcrumbs
    #
    def test_no_breadcrumbs_boxed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:no_breadcrumbs_boxed')),
            const.LAYOUT_NO_BREADCRUMBS_BOXED)

    def test_no_breadcrumbs_collapsed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:no_breadcrumbs_collapsed')),
            const.LAYOUT_NO_BREADCRUMBS_COLLAPSED)

    def test_no_breadcrumbs_fixed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:no_breadcrumbs_fixed')),
            const.LAYOUT_NO_BREADCRUMBS_FIXED)

    def test_no_breadcrumbs_top_nav(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:no_breadcrumbs_top_nav')),
            const.LAYOUT_NO_BREADCRUMBS_TOP_NAV)

    #
    #   No Breadcrumbs, No Footer
    #
    def test_no_breadcrumbs_footer_boxed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:no_breadcrumbs_footer_boxed')),
            const.LAYOUT_NO_BREADCRUMBS_FOOTER_BOXED)

    def test_no_breadcrumbs_footer_collapsed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:no_breadcrumbs_footer_collapsed')),
            const.LAYOUT_NO_BREADCRUMBS_FOOTER_COLLAPSED)

    def test_no_breadcrumbs_footer_fixed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:no_breadcrumbs_footer_fixed')),
            const.LAYOUT_NO_BREADCRUMBS_FOOTER_FIXED)

    def test_no_breadcrumbs_footer_top_nav(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:no_breadcrumbs_footer_top_nav')),
            const.LAYOUT_NO_BREADCRUMBS_FOOTER_TOP_NAV)

    #
    #   No Content Header
    #
    def test_no_content_header_boxed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:no_content_header_boxed')),
            const.LAYOUT_NO_CONTENT_HEADER_BOXED)

    def test_no_content_header_collapsed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:no_content_header_collapsed')),
            const.LAYOUT_NO_CONTENT_HEADER_COLLAPSED)

    def test_no_content_header_fixed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:no_content_header_fixed')),
            const.LAYOUT_NO_CONTENT_HEADER_FIXED)

    def test_no_content_header_top_nav(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:no_content_header_top_nav')),
            const.LAYOUT_NO_CONTENT_HEADER_TOP_NAV)

    #
    #   No Footer
    #
    def test_no_footer_boxed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:no_footer_boxed')),
            const.LAYOUT_NO_FOOTER_BOXED)

    def test_no_footer_collapsed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:no_footer_collapsed')),
            const.LAYOUT_NO_FOOTER_COLLAPSED)

    def test_no_footer_fixed(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:no_footer_fixed')),
            const.LAYOUT_NO_FOOTER_FIXED)

    def test_no_footer_top_nav(self):
        self.assertTemplateUsed(
            self.client.get(reverse('templates:no_footer_top_nav')),
            const.LAYOUT_NO_FOOTER_TOP_NAV)
