from django.conf.urls import url

from tests.views.gravatar_url import GravatarUrlInvalidDefaultTemplateView
from tests.views.gravatar_url import GravatarUrlInvalidRatingTemplateView
from tests.views.gravatar_url import GravatarUrlInvalidSizeMaxTemplateView
from tests.views.gravatar_url import GravatarUrlInvalidSizeMinTemplateView
from tests.views.gravatar_url import GravatarUrlTemplateView

app_name = 'gravatar_url'

urlpatterns = [
    url('invalid-default', GravatarUrlInvalidDefaultTemplateView.as_view(), name='invalid_default'),
    url('invalid-rating', GravatarUrlInvalidRatingTemplateView.as_view(), name='invalid_rating'),
    url('invalid-size-max', GravatarUrlInvalidSizeMaxTemplateView.as_view(), name='invalid_size_max'),
    url('invalid-size-min', GravatarUrlInvalidSizeMinTemplateView.as_view(), name='invalid_size_min'),
    url('', GravatarUrlTemplateView.as_view(), name='index'),
]
