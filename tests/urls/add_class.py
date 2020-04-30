from django.conf.urls import url

from tests.views.add_class import AddClassFormView

app_name = 'add_class'

urlpatterns = [
    url('', AddClassFormView.as_view(), name='index'),
]
