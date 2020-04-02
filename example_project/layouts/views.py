from django.views.generic import FormView
from django.views.generic import TemplateView

from .forms import LoginForm
from .forms import RegisterForm


class IndexView(TemplateView):
    template_name = 'layouts/index.html'


class BoxedView(TemplateView):
    template_name = 'layouts/boxed.html'


class CollapsedSidebarView(TemplateView):
    template_name = 'layouts/collapsed_sidebar.html'


class FixedView(TemplateView):
    template_name = 'layouts/fixed.html'


class TopNavigationView(TemplateView):
    template_name = 'layouts/top_navigation.html'


class LoginView(FormView):
    template_name = 'layouts/login.html'
    form_class = LoginForm


class RegisterView(FormView):
    template_name = 'layouts/register.html'
    form_class = RegisterForm
