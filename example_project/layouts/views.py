from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.views.generic import TemplateView


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
    form_class = AuthenticationForm


class RegisterView(FormView):
    template_name = 'layouts/register.html'
    form_class = UserCreationForm
