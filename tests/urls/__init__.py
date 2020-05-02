from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url(r'^add-active/', include('tests.urls.add_active')),
    url(r'^add-class/', include('tests.urls.add_class')),
    url(r'^gravatar-url/', include('tests.urls.gravatar_url')),
    url(r'^page-title/', include('tests.urls.page_title')),
    url(r'^paginator/', include('tests.urls.paginator')),
    url(r'^templates/', include('tests.urls.templates')),
]
