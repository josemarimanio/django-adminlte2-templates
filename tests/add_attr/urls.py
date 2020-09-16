from django.conf.urls import url

from . import views

app_name = 'add_attr'

urlpatterns = [
    url('',
        views.AddAttrFormView.as_view(), name='index'),
]
