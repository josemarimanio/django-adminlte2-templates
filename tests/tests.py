from django.contrib.auth.models import User
from django.contrib.sites.models import Site
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
        self.assertContains(self.response_child, '<p id="with-active"> active </p>', html=True)

    def test_without_active(self):
        self.assertContains(self.response_index, '<p id="without-active"></p>', html=True)

    def test_exact_match_true(self):
        self.assertContains(self.response_child, '<p id="exact-match-true"></p>', html=True)

    def test_exact_match_false(self):
        self.assertContains(self.response_child, '<p id="exact-match-false"> active </p>', html=True)

    def test_not_when_with_match(self):
        self.assertContains(self.response_index, '<p id="not-when-with-match"></p>', html=True)

    def test_not_when_with_match_multiple_parameters(self):
        self.assertContains(self.response_index, '<p id="not-when-with-match-multiple"></p>', html=True)

    def test_not_when_without_match(self):
        self.assertContains(self.response_index, '<p id="not-when-without-match"> active </p>', html=True)

    def test_detailview_pk(self):
        self.assertContains(self.response_pk, '<p id="detailview-pk"> active </p>', html=True)


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


class PaginatorTestCase(TestCase):
    """
    Test cases for {% paginator %} template tag
    """
    URL_PATTERN = 'paginator:index'

    def setUp(self):
        self.client = Client()
        for n in range(5):
            n = str(n)
            Site.objects.create(domain=n, name=n)

    def get_response_page(self, page):
        return self.client.get(reverse(self.URL_PATTERN) + '?page=' + str(page))

    #
    #   Sanity check
    #
    def test_response_page_1(self):
        self.assertContains(self.get_response_page(1),
                            '''<div id="check"><nav>
                                    <ul id="pagination" class="pagination">
                                        <li class="active"><a href="?page=1">1</a></li>
                                        <li><a href="?page=2">2</a></li>
                                        <li><a href="?page=3">3</a></li>
                                        <li><a href="?page=2"><i class="fa fa-caret-right"></i></a></li>
                                        <li><a href="?page=last"><small>Last</small></a></li>
                                    </ul>
                                </nav></div>''', html=True)

    def test_response_page_2(self):
        self.assertContains(self.get_response_page(2),
                            '''<div id="check"><nav>
                                    <ul id="pagination" class="pagination">
                                        <li><a href="?page=1"><small>First</small></a></li>
                                        <li><a href="?page=1"><i class="fa fa-caret-left"></i></a></li>
                                        <li><a href="?page=1">1</a></li>
                                        <li class="active"><a href="?page=2">2</a></li>
                                        <li><a href="?page=3">3</a></li>
                                        <li><a href="?page=4">4</a></li>
                                        <li><a href="?page=3"><i class="fa fa-caret-right"></i></a></li>
                                        <li><a href="?page=last"><small>Last</small></a></li>
                                    </ul>
                                </nav></div>''', html=True)

    def test_response_page_3(self):
        self.assertContains(self.get_response_page(3),
                            '''<div id="check"><nav>
                                    <ul id="pagination" class="pagination">
                                        <li><a href="?page=1"><small>First</small></a></li>
                                        <li><a href="?page=2"><i class="fa fa-caret-left"></i></a></li>
                                        <li><a href="?page=1">1</a></li>
                                        <li><a href="?page=2">2</a></li>
                                        <li class="active"><a href="?page=3">3</a></li>
                                        <li><a href="?page=4">4</a></li>
                                        <li><a href="?page=5">5</a></li>
                                        <li><a href="?page=4"><i class="fa fa-caret-right"></i></a></li>
                                        <li><a href="?page=last"><small>Last</small></a></li>
                                    </ul>
                                </nav></div>''', html=True)

    def test_response_page_4(self):
        self.assertContains(self.get_response_page(4),
                            '''<div id="check"><nav>
                                    <ul id="pagination" class="pagination">
                                        <li><a href="?page=1"><small>First</small></a></li>
                                        <li><a href="?page=3"><i class="fa fa-caret-left"></i></a></li>
                                        <li><a href="?page=2">2</a></li>
                                        <li><a href="?page=3">3</a></li>
                                        <li class="active"><a href="?page=4">4</a></li>
                                        <li><a href="?page=5">5</a></li>
                                        <li><a href="?page=6">6</a></li>
                                        <li><a href="?page=5"><i class="fa fa-caret-right"></i></a></li>
                                        <li><a href="?page=last"><small>Last</small></a></li>
                                    </ul>
                                </nav></div>''', html=True)

    def test_response_page_last(self):
        self.assertContains(self.get_response_page('last'),
                            '''<div id="check"><nav>
                                    <ul id="pagination" class="pagination">
                                        <li><a href="?page=1"><small>First</small></a></li>
                                        <li><a href="?page=5"><i class="fa fa-caret-left"></i></a></li>
                                        <li><a href="?page=4">4</a></li>
                                        <li><a href="?page=5">5</a></li>
                                        <li class="active"><a href="?page=6">6</a></li>
                                    </ul>
                                </nav></div>''', html=True)

    #
    #   'adjacent_pages' parameter to 3
    #
    def test_param_adjacent_pages_page_1(self):
        self.assertContains(self.get_response_page(1),
                            '''<div id="param-adjacent-pages"><nav>
                                    <ul id="pagination" class="pagination">
                                        <li class="active"><a href="?page=1">1</a></li>
                                        <li><a href="?page=2">2</a></li>
                                        <li><a href="?page=3">3</a></li>
                                        <li><a href="?page=4">4</a></li>
                                        <li><a href="?page=2"><i class="fa fa-caret-right"></i></a></li>
                                        <li><a href="?page=last"><small>Last</small></a></li>
                                    </ul>
                                </nav></div>''', html=True)

    def test_param_adjacent_pages_page_2(self):
        self.assertContains(self.get_response_page(2),
                            '''<div id="param-adjacent-pages"><nav>
                                    <ul id="pagination" class="pagination">
                                        <li><a href="?page=1"><small>First</small></a></li>
                                        <li><a href="?page=1"><i class="fa fa-caret-left"></i></a></li>
                                        <li><a href="?page=1">1</a></li>
                                        <li class="active"><a href="?page=2">2</a></li>
                                        <li><a href="?page=3">3</a></li>
                                        <li><a href="?page=4">4</a></li>
                                        <li><a href="?page=5">5</a></li>
                                        <li><a href="?page=3"><i class="fa fa-caret-right"></i></a></li>
                                        <li><a href="?page=last"><small>Last</small></a></li>
                                    </ul>
                                </nav></div>''', html=True)

    def test_param_adjacent_pages_page_3(self):
        self.assertContains(self.get_response_page(3),
                            '''<div id="param-adjacent-pages"><nav>
                                    <ul id="pagination" class="pagination">
                                        <li><a href="?page=1"><small>First</small></a></li>
                                        <li><a href="?page=2"><i class="fa fa-caret-left"></i></a></li>
                                        <li><a href="?page=1">1</a></li>
                                        <li><a href="?page=2">2</a></li>
                                        <li class="active"><a href="?page=3">3</a></li>
                                        <li><a href="?page=4">4</a></li>
                                        <li><a href="?page=5">5</a></li>
                                        <li><a href="?page=6">6</a></li>
                                        <li><a href="?page=4"><i class="fa fa-caret-right"></i></a></li>
                                        <li><a href="?page=last"><small>Last</small></a></li>
                                    </ul>
                                </nav></div>''', html=True)

    def test_param_adjacent_pages_page_4(self):
        self.assertContains(self.get_response_page(4),
                            '''<div id="param-adjacent-pages"><nav>
                                    <ul id="pagination" class="pagination">
                                        <li><a href="?page=1"><small>First</small></a></li>
                                        <li><a href="?page=3"><i class="fa fa-caret-left"></i></a></li>
                                        <li><a href="?page=1">1</a></li>
                                        <li><a href="?page=2">2</a></li>
                                        <li><a href="?page=3">3</a></li>
                                        <li class="active"><a href="?page=4">4</a></li>
                                        <li><a href="?page=5">5</a></li>
                                        <li><a href="?page=6">6</a></li>
                                        <li><a href="?page=5"><i class="fa fa-caret-right"></i></a></li>
                                        <li><a href="?page=last"><small>Last</small></a></li>
                                    </ul>
                                </nav></div>''', html=True)

    def test_param_adjacent_pages_last(self):
        self.assertContains(self.get_response_page('last'),
                            '''<div id="param-adjacent-pages"><nav>
                                    <ul id="pagination" class="pagination">
                                        <li><a href="?page=1"><small>First</small></a></li>
                                        <li><a href="?page=5"><i class="fa fa-caret-left"></i></a></li>
                                        <li><a href="?page=3">3</a></li>
                                        <li><a href="?page=4">4</a></li>
                                        <li><a href="?page=5">5</a></li>
                                        <li class="active"><a href="?page=6">6</a></li>
                                    </ul>
                                </nav></div>''', html=True)

    #
    #   'align' parameter choices
    #
    def test_param_align_initial(self):
        self.assertContains(self.get_response_page(1),
                            '''<div id="param-align-initial"><nav>
                                    <ul id="pagination" class="pagination">
                                        <li class="active"><a href="?page=1">1</a></li>
                                        <li><a href="?page=2">2</a></li>
                                        <li><a href="?page=3">3</a></li>
                                        <li><a href="?page=2"><i class="fa fa-caret-right"></i></a></li>
                                        <li><a href="?page=last"><small>Last</small></a></li>
                                    </ul>
                                </nav></div>''', html=True)

    def test_param_align_center(self):
        self.assertContains(self.get_response_page(1),
                            '''<div id="param-align-center"><nav class="text-center">
                                    <ul id="pagination" class="pagination">
                                        <li class="active"><a href="?page=1">1</a></li>
                                        <li><a href="?page=2">2</a></li>
                                        <li><a href="?page=3">3</a></li>
                                        <li><a href="?page=2"><i class="fa fa-caret-right"></i></a></li>
                                        <li><a href="?page=last"><small>Last</small></a></li>
                                    </ul>
                                </nav></div>''', html=True)

    def test_param_align_left(self):
        self.assertContains(self.get_response_page(1),
                            '''<div id="param-align-left"><nav class="pull-left">
                                    <ul id="pagination" class="pagination">
                                        <li class="active"><a href="?page=1">1</a></li>
                                        <li><a href="?page=2">2</a></li>
                                        <li><a href="?page=3">3</a></li>
                                        <li><a href="?page=2"><i class="fa fa-caret-right"></i></a></li>
                                        <li><a href="?page=last"><small>Last</small></a></li>
                                    </ul>
                                </nav></div>''', html=True)

    def test_param_align_right(self):
        self.assertContains(self.get_response_page(1),
                            '''<div id="param-align-right"><nav class="pull-right">
                                    <ul id="pagination" class="pagination">
                                        <li class="active"><a href="?page=1">1</a></li>
                                        <li><a href="?page=2">2</a></li>
                                        <li><a href="?page=3">3</a></li>
                                        <li><a href="?page=2"><i class="fa fa-caret-right"></i></a></li>
                                        <li><a href="?page=last"><small>Last</small></a></li>
                                    </ul>
                                </nav></div>''', html=True)

    #
    #   'no_margin' parameter
    #
    def test_param_no_margin_false(self):
        self.assertContains(self.get_response_page(1),
                            '''<div id="param-no-margin-false"><nav>
                                    <ul id="pagination" class="pagination">
                                        <li class="active"><a href="?page=1">1</a></li>
                                        <li><a href="?page=2">2</a></li>
                                        <li><a href="?page=3">3</a></li>
                                        <li><a href="?page=2"><i class="fa fa-caret-right"></i></a></li>
                                        <li><a href="?page=last"><small>Last</small></a></li>
                                    </ul>
                                </nav></div>''', html=True)

    def test_param_no_margin_true(self):
        self.assertContains(self.get_response_page(1),
                            '''<div id="param-no-margin-true"><nav>
                                    <ul id="pagination" class="pagination no-margin">
                                        <li class="active"><a href="?page=1">1</a></li>
                                        <li><a href="?page=2">2</a></li>
                                        <li><a href="?page=3">3</a></li>
                                        <li><a href="?page=2"><i class="fa fa-caret-right"></i></a></li>
                                        <li><a href="?page=last"><small>Last</small></a></li>
                                    </ul>
                                </nav></div>''', html=True)

    #
    #   Test all parameters
    #
    def test_param_all(self):
        self.assertContains(self.get_response_page(1),
                            '''<div id="all-params"><nav>
                                    <ul id="pagination" class="pagination">
                                        <li class="active"><a href="?page=1">1</a></li>
                                        <li><a href="?page=2">2</a></li>
                                        <li><a href="?page=3">3</a></li>
                                        <li><a href="?page=2"><i class="fa fa-caret-right"></i></a></li>
                                        <li><a href="?page=last"><small>Last</small></a></li>
                                    </ul>
                                </nav></div>''', html=True)


class PageTitleTestCase(TestCase):
    """
    Test cases for {% page_title %} template tag
    """
    URL_PATTERN_INDEX = 'page_title:index'
    URL_PATTERN_LIST = 'page_title:list'
    URL_PATTERN_OVERRIDE = 'page_title:override'

    def setUp(self):
        self.client = Client()

    def add_sites(self):
        # Add 2 items to 'Site' model
        for n in range(2):
            Site.objects.create(name=str(n), domain=str(n))

    def get_response_index(self):
        return self.client.get(reverse(self.URL_PATTERN_INDEX))

    def get_response_list(self, page='1'):
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
            return self.assertContains(self.get_response_list(), 'AdminLTE | Title (1 of 1)')

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
        Site.objects.create(domain='testserver', name='Site')
        return self.assertContains(self.get_response_index(), 'Site | Title')

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
