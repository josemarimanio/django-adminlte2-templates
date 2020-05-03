from django.contrib.sites.models import Site
from django.views.generic import DetailView
from django.views.generic import TemplateView


class AddActiveTemplateView(TemplateView):
    template_name = 'add_active/add_active.html'


class AddActiveDetailView(DetailView):
    model = Site
    template_name = 'add_active/add_active.html'
