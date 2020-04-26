from django.conf.urls import url

from tests.views.page_title import PageTitleListView
from tests.views.page_title import PageTitleTemplateView
from tests.views.page_title import PageTitleOverridePageNameTemplateView

app_name = 'page_title'

urlpatterns = [
    url(r'^list/$', PageTitleListView.as_view(), name='list'),
    url(r'^override/$', PageTitleOverridePageNameTemplateView.as_view(), name='override'),
    url('', PageTitleTemplateView.as_view(), name='index'),
]
