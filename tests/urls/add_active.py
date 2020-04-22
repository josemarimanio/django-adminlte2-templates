from django.conf.urls import url

from tests.views.add_active import AddActiveDetailView
from tests.views.add_active import AddActiveTemplateView

app_name = 'add_active'

urlpatterns = [
    url(r'^child/$', AddActiveTemplateView.as_view(), name='child'),
    url(r'^(?P<pk>\d+)/$', AddActiveDetailView.as_view(), name='pk'),
    url('', AddActiveTemplateView.as_view(), name='index'),
]
