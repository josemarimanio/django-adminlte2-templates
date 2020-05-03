from django.contrib.auth.models import User
from django.template.exceptions import TemplateSyntaxError
from django.test import Client
from django.test import TestCase

from adminlte2_templates.core import reverse


class GravatarUrlTestCase(TestCase):
    """
    Test cases for {% gravatar_url %} template tag

    Testing these cases for both authenticated and non-authenticated clients:

        * Sanity check
        * 'size', 'default', 'force_default', 'rating' 'user' params
        * 'ADMINLTE_GRAVATAR_SIZE','ADMINLTE_GRAVATAR_DEFAULT',
            'ADMINLTE_GRAVATAR_FORCE_DEFAULT' 'ADMINLTE_GRAVATAR_RATING' settings
        * Overriding settings with params
        * Raising TemplateSyntaxError on invalid 'size', 'default', 'rating' params
    """
    URL_PATTERN_INDEX = 'gravatar_url:index'
    URL_PATTERN_INVALID_DEFAULT = 'gravatar_url:invalid_default'
    URL_PATTERN_INVALID_SIZE_MAX = 'gravatar_url:invalid_size_max'
    URL_PATTERN_INVALID_SIZE_MIN = 'gravatar_url:invalid_size_min'
    URL_PATTERN_INVALID_RATING = 'gravatar_url:invalid_rating'

    USER_USERNAME = 'mari'
    USER_EMAIL = 'josemari.manio@gmail.com'
    USER_PASSWORD = 'maripassword'  # nosec

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(self.USER_USERNAME, self.USER_EMAIL, self.USER_PASSWORD)

    def get_response_with_auth(self):
        self.client.login(username=self.USER_USERNAME, password=self.USER_PASSWORD)
        return self.client.get(reverse(self.URL_PATTERN_INDEX))

    def get_response_without_auth(self):
        return self.client.get(reverse(self.URL_PATTERN_INDEX))

    def get_response_invalid_default(self):
        return self.client.get(reverse(self.URL_PATTERN_INVALID_DEFAULT))

    def get_response_invalid_size_max(self):
        return self.client.get(reverse(self.URL_PATTERN_INVALID_SIZE_MAX))

    def get_response_invalid_size_min(self):
        return self.client.get(reverse(self.URL_PATTERN_INVALID_SIZE_MIN))

    def get_response_invalid_rating(self):
        return self.client.get(reverse(self.URL_PATTERN_INVALID_RATING))

    #
    #   With authentication
    #
    def test_with_auth(self):
        self.assertContains(self.get_response_with_auth(), '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                                           '/b88d14ec6a751900484d421f8303824f?s=80&d=mp&r=pg&f=">',
                            html=True)

    # Tag parameters
    def test_with_auth_tag_param_size(self):
        self.assertContains(self.get_response_with_auth(), '<img id="param-size" src="https://www.gravatar.com/avatar'
                                                           '/b88d14ec6a751900484d421f8303824f?s=100&d=mp&r=pg&f=">',
                            html=True)

    def test_with_auth_tag_param_default(self):
        self.assertContains(self.get_response_with_auth(),
                            '<img id="param-default" src="https://www.gravatar.com/avatar'
                            '/b88d14ec6a751900484d421f8303824f?s=80&d=retro&r=pg&f=">', html=True)

    def test_with_auth_tag_param_force_default(self):
        self.assertContains(self.get_response_with_auth(),
                            '<img id="param-force-default" src="https://www.gravatar.com/avatar'
                            '/b88d14ec6a751900484d421f8303824f?s=80&d=mp&r=pg&f=y">', html=True)

    def test_with_auth_tag_param_rating(self):
        self.assertContains(self.get_response_with_auth(), '<img id="param-rating" src="https://www.gravatar.com/avatar'
                                                           '/b88d14ec6a751900484d421f8303824f?s=80&d=mp&r=r&f=">',
                            html=True)

    def test_with_auth_tag_param_user(self):
        self.assertContains(self.get_response_with_auth(), '<img id="param-user" src="https://www.gravatar.com/avatar'
                                                           '/b88d14ec6a751900484d421f8303824f?s=80&d=mp&r=pg&f=">',
                            html=True)

    def test_with_auth_tag_param_all(self):
        self.assertContains(self.get_response_with_auth(), '<img id="all-params" src="https://www.gravatar.com/avatar'
                                                           '/b88d14ec6a751900484d421f8303824f?s=100&d=retro&r=r&f=y">',
                            html=True)

    # Settings
    def test_with_auth_settings_param_size(self):
        with self.settings(ADMINLTE_GRAVATAR_SIZE=100):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=100&d=mp&r=pg&f=">', html=True)

    def test_with_auth_settings_param_default(self):
        with self.settings(ADMINLTE_GRAVATAR_DEFAULT='retro'):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=80&d=retro&r=pg&f=">', html=True)

    def test_with_auth_settings_param_force_default(self):
        with self.settings(ADMINLTE_GRAVATAR_FORCE_DEFAULT=True):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=80&d=mp&r=pg&f=y">', html=True)

    def test_with_auth_settings_param_rating(self):
        with self.settings(ADMINLTE_GRAVATAR_RATING='r'):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=80&d=mp&r=r&f=">', html=True)

    def test_with_auth_settings_param_all(self):
        with self.settings(ADMINLTE_GRAVATAR_SIZE=100, ADMINLTE_GRAVATAR_DEFAULT='retro',
                           ADMINLTE_GRAVATAR_FORCE_DEFAULT=True, ADMINLTE_GRAVATAR_RATING='r'):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=100&d=retro&r=r&f=y">', html=True)

    # Overriding settings with tag parameters
    def test_with_auth_override_settings_with_tag_param_size(self):
        with self.settings(ADMINLTE_GRAVATAR_SIZE=80):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="param-size" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=100&d=mp&r=pg&f=">', html=True)

    def test_with_auth_override_settings_with_tag_param_default(self):
        with self.settings(ADMINLTE_GRAVATAR_DEFAULT='mp'):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="param-default" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=80&d=retro&r=pg&f=">', html=True)

    def test_with_auth_override_settings_with_tag_param_force_default(self):
        with self.settings(ADMINLTE_GRAVATAR_FORCE_DEFAULT=False):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="param-force-default" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=80&d=mp&r=pg&f=y">', html=True)

    def test_with_auth_override_settings_with_tag_param_rating(self):
        with self.settings(ADMINLTE_GRAVATAR_RATING='pg'):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="param-rating" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=80&d=mp&r=r&f=">', html=True)

    def test_with_auth_override_settings_with_tag_param_all(self):
        with self.settings(ADMINLTE_GRAVATAR_SIZE=80, ADMINLTE_GRAVATAR_DEFAULT='mp',
                           ADMINLTE_GRAVATAR_FORCE_DEFAULT=False, ADMINLTE_GRAVATAR_RATING='pg'):
            self.assertContains(self.get_response_with_auth(),
                                '<img id="all-params" src="https://www.gravatar.com/avatar'
                                '/b88d14ec6a751900484d421f8303824f?s=100&d=retro&r=r&f=y">', html=True)

    #
    #   Without authentication
    #
    def test_without_auth(self):
        self.assertContains(self.get_response_without_auth(), 'https://www.gravatar.com/avatar/?s=80&d=mp&r=pg&f')

    # Tag parameters
    def test_without_auth_tag_param_size(self):
        self.assertContains(self.get_response_without_auth(),
                            '<img id="param-size" src="https://www.gravatar.com/avatar'
                            '/?s=100&d=mp&r=pg&f=">', html=True)

    def test_without_auth_tag_param_default(self):
        self.assertContains(self.get_response_without_auth(),
                            '<img id="param-default" src="https://www.gravatar.com/avatar'
                            '/?s=80&d=retro&r=pg&f=">', html=True)

    def test_without_auth_tag_param_force_default(self):
        self.assertContains(self.get_response_without_auth(),
                            '<img id="param-force-default" src="https://www.gravatar.com/avatar'
                            '/?s=80&d=mp&r=pg&f=y">', html=True)

    def test_without_auth_tag_param_rating(self):
        self.assertContains(self.get_response_without_auth(),
                            '<img id="param-rating" src="https://www.gravatar.com/avatar'
                            '/?s=80&d=mp&r=r&f=">', html=True)

    def test_without_auth_tag_param_user(self):
        self.assertContains(self.get_response_without_auth(),
                            '<img id="param-user" src="https://www.gravatar.com/avatar'
                            '/?s=80&d=mp&r=pg&f=">', html=True)

    def test_without_auth_tag_param_all(self):
        self.assertContains(self.get_response_without_auth(),
                            '<img id="all-params" src="https://www.gravatar.com/avatar'
                            '/?s=100&d=retro&r=r&f=y">', html=True)

    # Settings
    def test_without_auth_settings_param_size(self):
        with self.settings(ADMINLTE_GRAVATAR_SIZE=100):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/?s=100&d=mp&r=pg&f=">', html=True)

    def test_without_auth_settings_param_default(self):
        with self.settings(ADMINLTE_GRAVATAR_DEFAULT='retro'):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/?s=80&d=retro&r=pg&f=">', html=True)

    def test_without_auth_settings_param_force_default(self):
        with self.settings(ADMINLTE_GRAVATAR_FORCE_DEFAULT=True):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/?s=80&d=mp&r=pg&f=y">', html=True)

    def test_without_auth_settings_param_rating(self):
        with self.settings(ADMINLTE_GRAVATAR_RATING='r'):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="check-auth" src="https://www.gravatar.com/avatar'
                                '/?s=80&d=mp&r=r&f=">', html=True)

    # Override settings with tag parameters
    def test_without_auth_override_settings_with_tag_param_size(self):
        with self.settings(ADMINLTE_GRAVATAR_SIZE=80):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="param-size" src="https://www.gravatar.com/avatar'
                                '/?s=100&d=mp&r=pg&f=">', html=True)

    def test_without_auth_override_settings_with_tag_param_default(self):
        with self.settings(ADMINLTE_GRAVATAR_DEFAULT='mp'):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="param-default" src="https://www.gravatar.com/avatar'
                                '/?s=80&d=retro&r=pg&f=">', html=True)

    def test_without_auth_override_settings_with_tag_param_force_default(self):
        with self.settings(ADMINLTE_GRAVATAR_FORCE_DEFAULT=False):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="param-force-default" src="https://www.gravatar.com/avatar'
                                '/?s=80&d=mp&r=pg&f=y">', html=True)

    def test_without_auth_override_settings_with_tag_param_rating(self):
        with self.settings(ADMINLTE_GRAVATAR_RATING='pg'):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="param-rating" src="https://www.gravatar.com/avatar'
                                '/?s=80&d=mp&r=r&f=">', html=True)

    def test_without_auth_override_settings_with_tag_param_all(self):
        with self.settings(ADMINLTE_GRAVATAR_SIZE=80, ADMINLTE_GRAVATAR_DEFAULT='mp',
                           ADMINLTE_GRAVATAR_FORCE_DEFAULT=False, ADMINLTE_GRAVATAR_RATING='pg'):
            self.assertContains(self.get_response_without_auth(),
                                '<img id="all-params" src="https://www.gravatar.com/avatar'
                                '/?s=100&d=retro&r=r&f=y">', html=True)

    #
    #   Invalid parameters
    #
    def test_invalid_param_default(self):
        self.assertRaises(TemplateSyntaxError, self.get_response_invalid_default)

    def test_invalid_param_size_above_maximum(self):
        self.assertRaises(TemplateSyntaxError, self.get_response_invalid_size_max)

    def test_invalid_param_size_below_minimum(self):
        self.assertRaises(TemplateSyntaxError, self.get_response_invalid_size_min)

    def test_invalid_param_rating(self):
        self.assertRaises(TemplateSyntaxError, self.get_response_invalid_rating)
