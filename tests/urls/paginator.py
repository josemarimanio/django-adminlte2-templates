from django.conf.urls import url

from tests.views.paginator import PaginatorListView

app_name = 'paginator'

urlpatterns = [
    url('', PaginatorListView.as_view(), name='index'),
]
