from django.conf.urls import url

from . import views

app_name = 'gravatar_url'

urlpatterns = [
    url(r'^invalid-default/$',
        views.GravatarUrlInvalidDefaultTemplateView.as_view(), name='invalid_default'),
    url(r'^invalid-rating/$',
        views.GravatarUrlInvalidRatingTemplateView.as_view(), name='invalid_rating'),
    url(r'^invalid-size-max/$',
        views.GravatarUrlInvalidSizeMaxTemplateView.as_view(), name='invalid_size_max'),
    url(r'^invalid-size-min/$',
        views.GravatarUrlInvalidSizeMinTemplateView.as_view(), name='invalid_size_min'),
    url('',
        views.GravatarUrlTemplateView.as_view(), name='index'),
]
