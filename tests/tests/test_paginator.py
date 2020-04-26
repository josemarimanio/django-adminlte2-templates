from tests.tests import *


class PaginatorTestCase(TestCase):
    """
    Test cases for {% paginator %} template tag

    Testing these cases:

        * Sanity check
        * 'adjacent_pages', 'align', 'no_margin' params
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
