from django.conf.urls import url

try:
    # Supports >=Django 2.0
    from django.urls import include
except ImportError:
    # Supports <=Django 1.1
    from django.conf.urls import include

urlpatterns = [
    url(r'^add-active/', include('tests.add_active.urls')),
    url(r'^add-class/', include('tests.add_class.urls')),
    url(r'^gravatar-url/', include('tests.gravatar_url.urls')),
    url(r'^page-title/', include('tests.page_title.urls')),
    url(r'^paginator/', include('tests.paginator.urls')),
    url(r'^layouts/', include('tests.layouts.urls')),
]
