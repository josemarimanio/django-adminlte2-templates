from django.contrib.sites.models import Site
from django.views.generic import ListView
from django.views.generic import TemplateView


class PageTitleTemplateView(TemplateView):
    template_name = 'page_title/page_title.html'


class PageTitleOverridePageNameTemplateView(PageTitleTemplateView):
    def get_context_data(self, **kwargs):
        context = super(PageTitleOverridePageNameTemplateView, self).get_context_data(**kwargs)
        context['page_name'] = 'Override'
        return context


class PageTitleListView(ListView):
    template_name = 'page_title/page_title.html'
    model = Site
    paginate_by = 1
