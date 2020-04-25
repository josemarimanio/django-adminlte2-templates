from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url('^add-active/', include('tests.urls.add_active')),
    url('^add-class/', include('tests.urls.add_class')),
    url('^gravatar-url/', include('tests.urls.gravatar_url')),
]
