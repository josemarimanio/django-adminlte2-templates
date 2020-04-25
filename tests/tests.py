from django.contrib.auth.models import User
from django.test import Client
from django.test import SimpleTestCase
from django.test import TestCase

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
        self.response_index = self.client.get(reverse('add_active:index'))  # /add-active/
        self.response_child = self.client.get(reverse('add_active:child'))  # /add-active/child/
        self.response_pk = self.client.get(reverse('add_active:pk', args=(1,)))  # /add-active/<pk>/

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


class AddClassTestCase(SimpleTestCase):
    """
    Test cases for 'add_class' template filter
    """

    def setUp(self):
        self.client = Client()
        self.response_index = self.client.get(reverse('add_class:index'))  # /add-class/

    def test_add_class(self):
        self.assertContains(self.response_index, 'add-class')


class GravatarUrlTestCase(TestCase):
    """
    Test cases for {% gravatar_url %} template tag

    Testing these cases for both authenticated and non-authenticated clients:

        * Sanity check
        * Tag parameter outputs
        * Settings variable outputs
        * Overriding settings variable with tag parameter
        * Fail-safe values
    """
    URL_PATTERN = 'gravatar_url:index'
    USER_USERNAME = 'mari'
    USER_EMAIL = 'josemari.manio@gmail.com'
    USER_PASSWORD = 'maripassword'

    def setUp(self):
        self.client = Client()

    def get_response_with_auth(self):
        self.user = User.objects.create_user(self.USER_USERNAME, self.USER_EMAIL, self.USER_PASSWORD)
        self.client.login(username=self.USER_USERNAME, password=self.USER_PASSWORD)
        return self.client.get(reverse(self.URL_PATTERN))

    def get_response_without_auth(self):
        return self.client.get(reverse(self.URL_PATTERN))

    #
    #   With authentication
    #
    def test_with_auth(self):
        self.assertContains(self.get_response_with_auth(), '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                                           '/b88d14ec6a751900484d421f8303824f?s=80&d=mp&r=pg&f=">')

    # Tag parameters
    def test_with_auth_tag_param_size(self):
        self.assertContains(self.get_response_with_auth(), '<img id="param-size" src="https://www.gravatar.com/avatar'
                                                           '/b88d14ec6a751900484d421f8303824f?s=100&d=mp&r=pg&f=">')

    def test_with_auth_tag_param_default(self):
        self.assertContains(self.get_response_with_auth(),
                            '<img id="param-default" src="https://www.gravatar.com/avatar'
                            '/b88d14ec6a751900484d421f8303824f?s=80&d=retro&r=pg&f=">')

    def test_with_auth_tag_param_force_default(self):
        self.assertContains(self.get_response_with_auth(),
                            '<img id="param-force-default" src="https://www.gravatar.com/avatar'
                            '/b88d14ec6a751900484d421f8303824f?s=80&d=mp&r=pg&f=y">')

    def test_with_auth_tag_param_rating(self):
        self.assertContains(self.get_response_with_auth(), '<img id="param-rating" src="https://www.gravatar.com/avatar'
                                                           '/b88d14ec6a751900484d421f8303824f?s=80&d=mp&r=r&f=">')

    def test_with_auth_tag_param_user(self):
        self.assertContains(self.get_response_with_auth(), '<img id="param-user" src="https://www.gravatar.com/avatar'
                                                           '/b88d14ec6a751900484d421f8303824f?s=80&d=mp&r=pg&f=">')

    def test_with_auth_tag_param_all(self):
        self.assertContains(self.get_response_with_auth(), '<img id="all-params" src="https://www.gravatar.com/avatar'
                                                           '/b88d14ec6a751900484d421f8303824f?s=100&d=retro&r=r&f=y">')

    # Settings
    def test_with_auth_settings_param_size(self):
        with self.settings(ADMINLTE_GRAVATAR_SIZE=100):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=100&d=mp&r=pg&f=">')

    def test_with_auth_settings_param_default(self):
        with self.settings(ADMINLTE_GRAVATAR_DEFAULT='retro'):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=80&d=retro&r=pg&f=">')

    def test_with_auth_settings_param_force_default(self):
        with self.settings(ADMINLTE_GRAVATAR_FORCE_DEFAULT=True):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=80&d=mp&r=pg&f=y">')

    def test_with_auth_settings_param_rating(self):
        with self.settings(ADMINLTE_GRAVATAR_RATING='r'):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=80&d=mp&r=r&f=">')

    def test_with_auth_settings_param_all(self):
        with self.settings(ADMINLTE_GRAVATAR_SIZE=100, ADMINLTE_GRAVATAR_DEFAULT='retro',
                           ADMINLTE_GRAVATAR_FORCE_DEFAULT=True, ADMINLTE_GRAVATAR_RATING='r'):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=100&d=retro&r=r&f=y">')

    # Overriding settings with tag parameters
    def test_with_auth_override_settings_with_tag_param_size(self):
        with self.settings(ADMINLTE_GRAVATAR_SIZE=80):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="param-size" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=100&d=mp&r=pg&f=">')

    def test_with_auth_override_settings_with_tag_param_default(self):
        with self.settings(ADMINLTE_GRAVATAR_DEFAULT='mp'):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="param-default" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=80&d=retro&r=pg&f=">')

    def test_with_auth_override_settings_with_tag_param_force_default(self):
        with self.settings(ADMINLTE_GRAVATAR_FORCE_DEFAULT=False):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="param-force-default" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=80&d=mp&r=pg&f=y">')

    def test_with_auth_override_settings_with_tag_param_rating(self):
        with self.settings(ADMINLTE_GRAVATAR_RATING='pg'):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="param-rating" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=80&d=mp&r=r&f=">')

    def test_with_auth_override_settings_with_tag_param_all(self):
        with self.settings(ADMINLTE_GRAVATAR_SIZE=80, ADMINLTE_GRAVATAR_DEFAULT='mp',
                           ADMINLTE_GRAVATAR_FORCE_DEFAULT=False, ADMINLTE_GRAVATAR_RATING='pg'):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="all-params" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=100&d=retro&r=r&f=y">')

    #
    #   Without authentication
    #
    def test_without_auth(self):
        self.assertContains(self.get_response_without_auth(), 'https://www.gravatar.com/avatar/?s=80&d=mp&r=pg&f')

    # Tag parameters
    def test_without_auth_tag_param_size(self):
        self.assertContains(self.get_response_without_auth(),
                            '<img id="param-size" src="https://www.gravatar.com/avatar'
                            '/?s=100&d=mp&r=pg&f=">')

    def test_without_auth_tag_param_default(self):
        self.assertContains(self.get_response_without_auth(),
                            '<img id="param-default" src="https://www.gravatar.com/avatar'
                            '/?s=80&d=retro&r=pg&f=">')

    def test_without_auth_tag_param_force_default(self):
        self.assertContains(self.get_response_without_auth(),
                            '<img id="param-force-default" src="https://www.gravatar.com/avatar'
                            '/?s=80&d=mp&r=pg&f=y">')

    def test_without_auth_tag_param_rating(self):
        self.assertContains(self.get_response_without_auth(),
                            '<img id="param-rating" src="https://www.gravatar.com/avatar'
                            '/?s=80&d=mp&r=r&f=">')

    def test_without_auth_tag_param_user(self):
        self.assertContains(self.get_response_without_auth(),
                            '<img id="param-user" src="https://www.gravatar.com/avatar'
                            '/?s=80&d=mp&r=pg&f=">')

    def test_without_auth_tag_param_all(self):
        self.assertContains(self.get_response_without_auth(),
                            '<img id="all-params" src="https://www.gravatar.com/avatar'
                            '/?s=100&d=retro&r=r&f=y">')

    # Settings
    def test_without_auth_settings_param_size(self):
        with self.settings(ADMINLTE_GRAVATAR_SIZE=100):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/?s=100&d=mp&r=pg&f=">')

    def test_without_auth_settings_param_default(self):
        with self.settings(ADMINLTE_GRAVATAR_DEFAULT='retro'):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/?s=80&d=retro&r=pg&f=">')

    def test_without_auth_settings_param_force_default(self):
        with self.settings(ADMINLTE_GRAVATAR_FORCE_DEFAULT=True):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/?s=80&d=mp&r=pg&f=y">')

    def test_without_auth_settings_param_rating(self):
        with self.settings(ADMINLTE_GRAVATAR_RATING='r'):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/?s=80&d=mp&r=r&f=">')

    # Override settings with tag parameters
    def test_without_auth_override_settings_with_tag_param_size(self):
        with self.settings(ADMINLTE_GRAVATAR_SIZE=80):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="param-size" src="https://www.gravatar.com/avatar'
                                '/?s=100&d=mp&r=pg&f=">')

    def test_without_auth_override_settings_with_tag_param_default(self):
        with self.settings(ADMINLTE_GRAVATAR_DEFAULT='mp'):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="param-default" src="https://www.gravatar.com/avatar'
                                '/?s=80&d=retro&r=pg&f=">')

    def test_without_auth_override_settings_with_tag_param_force_default(self):
        with self.settings(ADMINLTE_GRAVATAR_FORCE_DEFAULT=False):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="param-force-default" src="https://www.gravatar.com/avatar'
                                '/?s=80&d=mp&r=pg&f=y">')

    def test_without_auth_override_settings_with_tag_param_rating(self):
        with self.settings(ADMINLTE_GRAVATAR_RATING='pg'):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="param-rating" src="https://www.gravatar.com/avatar'
                                '/?s=80&d=mp&r=r&f=">')

    def test_without_auth_override_settings_with_tag_param_all(self):
        with self.settings(ADMINLTE_GRAVATAR_SIZE=80, ADMINLTE_GRAVATAR_DEFAULT='mp',
                           ADMINLTE_GRAVATAR_FORCE_DEFAULT=False, ADMINLTE_GRAVATAR_RATING='pg'):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="all-params" src="https://www.gravatar.com/avatar'
                                '/?s=100&d=retro&r=r&f=y">')
