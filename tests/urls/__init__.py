from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url('^add-active/', include('tests.urls.add_active')),
]
