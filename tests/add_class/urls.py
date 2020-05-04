from django.conf.urls import url

from . import views

app_name = 'add_class'

urlpatterns = [
    url('',
        views.AddClassFormView.as_view(), name='index'),
]
