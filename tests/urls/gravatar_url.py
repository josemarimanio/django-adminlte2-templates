from django.conf.urls import url

from tests.views.gravatar_url import GravatarUrlTemplateView

app_name = 'gravatar_url'

urlpatterns = [
    url('', GravatarUrlTemplateView.as_view(), name='index'),
]
