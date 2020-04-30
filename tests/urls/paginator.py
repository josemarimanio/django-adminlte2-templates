from django.conf.urls import url

from tests.views.paginator import PaginatorInvalidAdjacentPagesListView
from tests.views.paginator import PaginatorInvalidAlignListView
from tests.views.paginator import PaginatorListView

app_name = 'paginator'

urlpatterns = [
    url(r'^invalid-adjacent-pages/$', PaginatorInvalidAdjacentPagesListView.as_view(), name='invalid_adjacent_pages'),
    url(r'^invalid-align/$', PaginatorInvalidAlignListView.as_view(), name='invalid_align'),
    url('', PaginatorListView.as_view(), name='index'),
]
