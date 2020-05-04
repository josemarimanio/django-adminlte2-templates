from django.conf.urls import url

from . import views

app_name = 'page_title'

urlpatterns = [
    url(r'^list/$',
        views.PageTitleListView.as_view(), name='list'),
    url(r'^override/$',
        views.PageTitleOverridePageNameTemplateView.as_view(), name='override'),
    url('',
        views.PageTitleTemplateView.as_view(), name='index'),
]
