from django.urls import path

from layouts.views import BoxedView
from layouts.views import CollapsedSidebarView
from layouts.views import FixedView
from layouts.views import IndexView
from layouts.views import LoginView
from layouts.views import RegisterView
from layouts.views import TopNavigationView

app_name = 'layouts'

urlpatterns = [
    path('boxed', BoxedView.as_view(), name='boxed'),
    path('collapsed', CollapsedSidebarView.as_view(), name='collapsed'),
    path('fixed', FixedView.as_view(), name='fixed'),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('top-nav', TopNavigationView.as_view(), name='top_nav'),

    path('', IndexView.as_view(), name='index'),
]
