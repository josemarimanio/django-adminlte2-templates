from django.conf.urls import url

from . import views

app_name = 'paginator'

urlpatterns = [
    url(r'^invalid-adjacent-pages/$',
        views.PaginatorInvalidAdjacentPagesListView.as_view(), name='invalid_adjacent_pages'),
    url(r'^invalid-align/$',
        views.PaginatorInvalidAlignListView.as_view(), name='invalid_align'),
    url('',
        views.PaginatorListView.as_view(), name='index'),
]
